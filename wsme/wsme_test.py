from wsme import types as wstypes
from wsme.rest import json

result_type = wstypes.DictType(str, object)

print ''
result_val = {'std_out':{}, 'std_err':{}, 'exit_code':0}
print '(1). Validating result_val against result_type ... %s ' %  (result_type.validate(result_val) is not None)
print json.tojson(result_type, result_val)

print ''
result_val = {'localhost':{'std_out':'', 'std_err':'', 'exit_code':0}} 
print '(2). Validating result_val against result_type ... %s ' %  (result_type.validate(result_val) is not None)
print json.tojson(result_type, result_val)

print ''
result_val = {'localhost':{'std_out':'', 'std_err':'', 'exit_code':0}, '10.20.104.123':{'std_out':'', 'std_err':'', 'exit_code':0}} 
print '(3). Validating result_val against result_type ... %s ' %  (result_type.validate(result_val) is not None)
print json.tojson(result_type, result_val)

