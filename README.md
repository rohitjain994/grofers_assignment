## Use Case
As this design is based on subscription, So first step is to get subscription id.
### 1. GET Subscribe ID
Return 10 digit string consist of ascii characters
```
curl --location --request GET 'localhost:5000/api/v1/subscribe'
```
Output
```
hfmhpydiqm
```
### 2. POST Key:Value

2.a If you doesn't pass subscribe_id

```
curl --location --request POST 'localhost:5000/api/v1/putkeyvalue'
```
Output
```
Error: No subscribe_id field provided. Please specify an subscribe_id.
```

2.b If you pass wrong subscribe_id
```
curl --location --request GET 'localhost:5000/api/v1/putkeyvalue?subscribe_id=hfmhpydiqm1'

curl --location --request POST 'localhost:5000/api/v1/putkeyvalue?subscribe_id=hfmhpydiqm1&key=abc&value=qwerty'

```
Output
```
Error: Wrong subscribe_id. Please create new or existing subscription.
```
2.c if key field does not exist as argument
```
curl --location --request GET 'localhost:5000/api/v1/putkeyvalue?subscribe_id=hfmhpydiqm
```
Output
```
Error: No key field provided. Please specify an key.
```
2.d if value field does not exist
```
curl --location --request POST 'localhost:5000/api/v1/putkeyvalue?subscribe_id=hfmhpydiqm&key=abc'
```
Output
```
Error: No value field provided. Please specify an value.
```
2.e Successful Key Value post
```
curl --location --request POST 'localhost:5000/api/v1/putkeyvalue?subscribe_id=hfmhpydiqm&key=abc&value=qwerty'
```
Output
```
Success: key:value updated
```

### 3. GET Key

3.a If you doesn't pass subscribe_id

```
curl --location --request GET 'localhost:5000/api/v1/getkey'
```
Output
```
Error: No subscribe_id field provided. Please specify an subscribe_id.
```

3.b If you pass wrong subscribe_id
```
curl --location --request GET 'localhost:5000/api/v1/getkey?subscribe_id=hfmhpydiqm1'
```
Output
```
Error: Wrong subscribe_id. Please create new or existing subscription.
```
3.c if key field does not exist as argument
```
curl --location --request GET 'localhost:5000/api/v1/getkey?subscribe_id=hfmhpydiqm
```
Output
```
Error: No key field provided. Please specify an key.
```
3.d if key does not exist
```
curl --location --request GET 'localhost:5000/api/v1/getkey?subscribe_id=hfmhpydiqm&key=abc'
```
Output
```
Error: Key does not exist
```
3.e Success key search
```
curl --location --request GET 'localhost:5000/api/v1/getkey?subscribe_id=hfmhpydiqm&key=abc'
```
output
```
qwerty
```
