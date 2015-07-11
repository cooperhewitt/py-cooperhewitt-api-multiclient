# py-cooperhewitt

Python bindings to the Cooper-Hewitt collections API with support for multiple parallel requests (using grequest).

## Installation

You can install this by either cloning this repository and running

```
$> python setup.py install
```

## Example

`cooperhewitt.api.multiclient` subclasses `cooperhewitt.api.client` and exports
a single additional `execute_methods` that takes a list of (method, args) tuples
and returns a generator (of standard `execute_method` responses.

```
import cooperhewitt.api.multiclient
import pprint

api = cooperhewitt.api.multiclient.OAuth2(ACCESS_TOKEN)

reqs = (
    ('cooperhewitt.labs.whatWouldMicahSay', {}),
    ('cooperhewitt.objects.getRandom', {'has_image': 1}),
    ('cooperhewitt.labs.whatWouldMicahSay', {}),
    ('cooperhewitt.objects.getRandom', {'has_image': 1}),
    ('cooperhewitt.labs.whatWouldMicahSay', {}),
    ('cooperhewitt.objects.getRandom', {'has_image': 1}),
)

for rsp in api.execute_methods(reqs):
    print pprint.pformat(rsp)

rsp = api.execute_method(*req[1]):
print pprint.pformat(rsp)

```
	
## See also

* [Smithsonian Cooper-Hewitt National Design Museum collections website](https://collection.cooperhewitt.org/)
* [Smithsonian Cooper-Hewitt National Design Museum collections API](https://collection.cooperhewitt.org/api/)


