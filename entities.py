entity=lambda name,attributesTypes: "type %s struct {\n%s\n}"%(name,'\n'.join([ attribute+' '+type for attribute, type in attributesTypes.items()]))


jsonKeyCase=lambda s:   s.lower() if s[1].isupper() else s[0].lower()+s[1:]



from collections import OrderedDict


d=OrderedDict()
with open("tmp","r") as f:
	for line in f:
		d[line.strip()]='string `json:"%s"`'%(jsonKeyCase(line.strip()))

print entity("SupplierContract",d)
