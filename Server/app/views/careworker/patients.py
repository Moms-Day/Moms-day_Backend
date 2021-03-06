import uuid

from flask import Blueprint, request, Response, abort
from flask_restful import Api
from flask_jwt_extended import get_jwt_identity
from flasgger import swag_from

from app.views import BaseResource, json_required, auth_required

from app.models.account import CareWorkerModel, DaughterModel
from app.models.connect import RequestModel
from app.models.patient import PatientModel

from app.docs.careworker.patients import *

api = Api(Blueprint(__name__, __name__))
api.prefix = '/care'


@api.resource('/patients')
class ViewPatientsList(BaseResource):
    @swag_from(CARE_VIEW_PATIENTS_LIST_GET)
    @auth_required(CareWorkerModel)
    def get(self):
        c = CareWorkerModel.objects(id=get_jwt_identity()).first()
        reqs = RequestModel.objects(care_worker=c)
        patients = PatientModel.objects(care_worker=c)
        data = {
            'connectionRequests': [{
                    'req_id': req.req_id,
                    'requester_id': req.requester_id,
                    'r_name': req.requester_name,
                    'p_name': req.patient_name,
                    'p_age': req.patient_age,
                    'p_gender': req.patient_gender,
                    'request_time': req.request_time
                } for req in reqs] if reqs else [],

            'inChargeList': [{
                'd_id': patient.daughter.id,
                'id': patient.id,
                'name': patient.name,
                'age': patient.age,
                'gender': patient.gender,
                'daughter': patient.daughter.name
            } for patient in patients] if patients else []
        }

        return self.unicode_safe_json_dumps(data, 200)

    @swag_from(CARE_ACCEPT_OR_REJECT_REQUESTS_PATCH)
    @auth_required(CareWorkerModel)
    @json_required({
        'id': str,
        'reqId': str,
        'accept': bool
    })
    def patch(self):
        accept = request.json['accept']
        requester = DaughterModel.objects(id=request.json['id']).first()
        req = RequestModel.objects(req_id=request.json['reqId']).first()
        myself = CareWorkerModel.objects(id=get_jwt_identity()).first()

        if not requester or not req:
            abort(400)

        if accept:
            PatientModel(
                id=str(uuid.uuid4()),
                name=req.patient_name,
                age=req.patient_age,
                gender=req.patient_gender,
                daughter=requester,
                care_worker=myself
            ).save()

        req.delete()

        return Response('', 201)


@api.resource('/patients/<p_id>')
class MemoAboutPatient(BaseResource):
    @swag_from(CARE_VIEW_PATIENT_MEMO_GET)
    @auth_required(CareWorkerModel)
    def get(self, p_id):
        return PatientModel.objects(id=p_id).first().memo, 200

    @swag_from(CARE_MODIFY_PATIENT_MEMO_PATCH)
    @auth_required(CareWorkerModel)
    @json_required({'memo': str})
    def patch(self, p_id):
        memo = request.json['memo']
        PatientModel.objects(id=p_id).first().update(memo=memo)

        return Response('', 201)
