docker build . -t rust-local-distroless

# Verify
docker images | grep rust-

docker run -it -p 8000:8000 rust-local-distroless  # -it: interactive

# Test
curl -X POST --data '{"text": "some text"}' \
     --header "Content-Type: application/json" \
     http://localhost:8000/tokenizers/bert-base-uncased
