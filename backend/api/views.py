# -*- coding: utf-8 -*-
from flask import Blueprint, json

from api.models import RiskType


api_views = Blueprint('api_views', __name__)


@api_views.route("/risk-types/")
@api_views.route("/risk-types/<int:risk_type_id>")
def risk_types(risk_type_id=None):
    if risk_type_id:
        risk_type = RiskType.query.filter_by(id=risk_type_id).first_or_404()
        return json.jsonify(risk_type.to_dict())
    return json.jsonify([risk.to_dict() for risk in RiskType.query.all()])
