# This is a basic e2e test that only validates status codes. For the real version, validate response payload as well.
BASE_URL=$API_BASE_URL

echo "Debug - API_BASE_URL environment variable: $API_BASE_URL"
echo "Debug - BASE_URL being used: $BASE_URL"

run_test() {
  local method="$1"
  local path="$2"
  local expected_status="$3"
  local data="{$4:-}"

  echo -e "\nTesting $method $path"

  # Send HTTP request
  if [[ -n "$data" ]]; then
    response=$(curl -s -X "$method" -H "Content-Type: application/json" -d "$data" -w "\nStatus: %{http_code}\n" -o /tmp/out.txt "$BASE_URL$path")
  else
    response=$(curl -s -X "$method" -w "\nStatus: %{http_code}\n" -o /tmp/out.txt "$BASE_URL$path")
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

run_test GET "/shows" 200

run_test GET "/shows/123" 200

run_test POST "/shows" 200 "{'name': 'Test Show'}"

run_test PUT "/shows/123" 200 "{'name': 'Updated Show'}"

run_test DELETE "/shows/123" 204

run_test GET "/invalid" 404
