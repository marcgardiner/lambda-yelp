import json

from yelpapi import YelpAPI
from log_writer import *

logger = get_logger('lambda-yelp')


def get_config(context):
	function_name = context.function_name
	function_arn = context.invoked_function_arn
	alias = function_arn.split(":").pop()

	config_file = '.json'

	if (alias == function_name or '$LATEST' == alias):
		config_file = 'dev' + config_file
	else:
		config_file = alias.lower() + config_file

	config_data = None
	with open(config_file) as json_data:
		config_data = json.load(json_data)

	return config_data


def handler(event, context):
	config_data = get_config(context)
	response = {'Status': 'success'}

	try:
		lat = event["lat"] if event["lat"] else 0
		long = event["long"] if event["long"] else 0
		name = event["name"] if event["name"] else ''
		limit = event["limit"] if event["limit"] else 50

		if (lat==0 or long==0 or name==''):
			logger.error('**ERROR: code.parameters.required')
			raise Exception()

		yelp_api = YelpAPI(config_data['yelp_api_key'])
		yelp_res = yelp_api.search_query(categories='restaurants', longitude=long, latitude=lat, limit=limit)
		for item in yelp_res['businesses']:
			logger.info('Location Name: {} and Rating: {}'.format(item['name'], item['rating']))

	except Exception as e:
		error(logger, e)
		response['Status'] = 'failure'

	return response
