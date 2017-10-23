RETRIES=15

echo "Trying to connect to 'postgres://postgres@postgres:5432'"
until psql postgres://postgres@postgres:5432 -c "select 1" > /dev/null 2>&1 || [ $RETRIES -eq 0 ]; do
  echo "Waiting for postgres server, $((RETRIES--)) remaining attempts..."
  sleep 1
done
