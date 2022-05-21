import json
import os

# config = {
#   'user': os.environ.get('DB_USER'),
#   'password': os.environ.get('DB_PWD'),
#   'host': os.environ.get('DB_HOST'),
#   'database': os.environ.get('DB_NAME'),
#   'raise_on_warnings': True
# }


def function_list():
  jsondata = ['something']
  return jsondata

# def panel_statements(panel_id, statement_type, speaker):
#   if panel_id != "N/A":
#     query = ("select statement,speaker,statement_time,statement_type from panel_statements where panel_id = '" + panel_id + "'")
#   elif statement_type != "N/A":
#     query = ("select a.panel_id,b.panel_title,a.speaker,a.statement,a.statement_time,a.statement_type from panel_statements a, panel_details b where a.panel_id=b.panel_id and a.statement_type = '" + statement_type + "'")
#   elif speaker != "N/A":
#     query = ("select a.panel_id,b.panel_title,a.speaker,a.statement,a.statement_time,a.statement_type from panel_statements a, panel_details b where a.panel_id=b.panel_id and a.speaker = '" + speaker + "'")
#   jsondata = get_query_results(query)
#   return jsondata

# def panel_search(searchstring):
#   query = ("select a.panel_id, b.panel_title, a.statement, a.speaker, a.statement_time, a.statement_type from panel_statements a, panel_details b where a.panel_id=b.panel_id and match(a.statement) against ('" + searchstring +"' in natural language mode)")
#   jsondata = get_query_results(query)
#   return jsondata