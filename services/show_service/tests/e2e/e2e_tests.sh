# This is a basic e2e test that only validates status codes. For the real version, validate response payload as well.

STACK_NAME="ShowService" # Should match up with samconfig.toml

echo "TESTING ..."
echo "AWS Region: $AWS_REGION"

API_BASE_URL=$(aws cloudformation describe-stacks \
  --stack-name "$STACK_NAME" \
  --query "Stacks[0].Outputs[?OutputKey=='HelloWorldApi'].OutputValue" \
  --region $AWS_REGION \
  --output text)

if [[ -z "$API_BASE_URL" ]]; then
  echo "API_BASE_URL is empty. Please check CloudFormation output."
  exit 1
fi

echo "API_BASE_URL: $API_BASE_URL"

run_test() {
  local method="$1"
  local path="$2"
  local expected_status="$3"
  local data="${4:-}"

  echo -e "\nTesting $method $path"

  # Send HTTP request
  if [[ -n "$data" ]]; then
    response=$(curl -s -X "$method" -H "Content-Type: application/json" -d "$data" -w "\nStatus: %{http_code}\n" -o /tmp/out.txt "$API_BASE_URL$path")
  else
    response=$(curl -s -X "$method" -w "\nStatus: %{http_code}\n" -o /tmp/out.txt "$API_BASE_URL$path")
  fi

  # Capture response payload and status code
  response_payload=$(cat /tmp/out.txt)
  status="${response: -3}"

  # Log response
  echo "Response: $response_payload"
  echo "Status Code: $status"

  # Assert that the status code matches the expected status code
  if [[ "$status" -eq "$expected_status" ]]; then
    echo "Test Passed!"
  else
    echo "Test Failed! Expected $expected_status but got $status."
    exit 1
  fi
}

# Tests

run_test GET "/" 200

run_test GET "/123" 200

run_test POST "/" 200 '{"name": "Test Show"}'

run_test PUT "/123" 200 '{"name": "Updated Show"}'

run_test DELETE "/123" 204

run_test PATCH "/invalid" 404
