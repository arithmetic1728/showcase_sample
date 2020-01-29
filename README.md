# 1. Download showcase server code.

First download the showcase server code.
```
git clone https://github.com/arithmetic1728/echo_sample.git
```

# 2. Test the sample client code.
## 2.1. Run the downloaded server code.

```
python echo_sample/handwritten/server.py
```
## 2.2. Install generated client.
First change to correct_client branch. The microgenerator has bug and this branch fixes the generated code.
```
git checkout correct_client
```

Install the generated showcase client package
```
cd showcase_generated
pip install --editable .
```

## 2.3. Now we can run the sample.
```
python ../sample/sample.py
```

# 3. Test the sample client with interceptors.
There are two tests, unary_stream and stream_stream.

## 3.1. Run the downloaded server code.

```
python echo_sample/handwritten/interceptor_stream_stream_server.py
```
or
```
python echo_sample/handwritten/interceptor_unary_stream_server.py
```

## 3.2 same as 2.2

## 3.3. Now we can run the sample.

```
python ../sample/stream_stream_interceptor_sample.py
```
or
```
python ../sample/unary_stream_interceptor_sample.py
```
