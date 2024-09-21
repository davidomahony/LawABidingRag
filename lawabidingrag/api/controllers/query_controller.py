from flask import Blueprint
from core.services.query_service import llm_query_service
from flask import request, jsonify

query_bp = Blueprint('query', __name__)



@query_bp.route('/query', methods=['POST'])
def query():
    data = request.get_json()
    querystring = data.get('querystring')
    context = data.get('context')
    model_used = data.get('modelUsed')
    
    if not querystring:
        return jsonify({"error": "querystring is required"}), 400
    
    service = llm_query_service()
    response = service.query(querystring)
    return jsonify(
        {
            "response": response,
            "model_used": model_used,
            "context": context
         })


@query_bp.route('/query/historical')
def query_historical():
    return 'Not supported yet!'

@query_bp.route('/query/prompttips')
def query_prompttips():
    return 'Not supported yet!'
