import boto3

dyndb = boto3.resource('dynamodb',
region_name='us-west-2',
aws_access_key_id='AKIAS2IKD2UAEDS4Q644', 
aws_secret_access_key='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'
)

exptable = dyndb.Table("ExpDataTable")
exptable.meta.client.get_waiter('table_exists').wait(TableName='ExpDataTable')

# query
for id in ['1', '2', '3']:
	response = exptable.get_item( 
	    Key={
	        'Id': id
	    }
	)
	print(response["Item"])