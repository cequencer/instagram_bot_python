import string
import random
import hmac
import config
import hashlib

def _generate_device(N):
	return ''.join([random.choice('0123456789ABCDEF') for x in range(N)])

def _generate_signature(data):
	return hmac.new(config.key.encode('utf-8'), data.encode('utf-8'), hashlib.sha256).hexdigest()

def _generate_body(data):
	token=_generate_signature(data)
	new_data='%s.%s'%(token,data)
	return {'signed_body':new_data,'ig_sig_key_version':'5'}