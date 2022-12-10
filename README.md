# send_later
send scheduler message to messanger api by Fast-Api

### Usage
I am using python "3.10.6" version 

first step clone my project
```
git clone https://github.com/sorooshm78/send_later/
```
go to [Eitaa API](https://eitaayar.ir/) website and generate token

so rename messanger/sample_tokens.json to messanger/tokens.json and copy your Token into file 
```
{
    "eitaa": "Your Eitaa Token"
}
```

and then install requirements  
```
pip install -r requirements.txt
```

### Running the code 
Just go into the code directory and type 
```
python main.py
```
"send_later" app will start on 127.0.0.1:8000 (Local Address).

and for read documents 127.0.0.1:8000/docs or 127.0.0.1:8000/redoc 
