#/bin/sh

workdir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

api_name='microservices_api'
catalog_service_path=$workdir/'catalog-service'
order_service_path=$workdir/'order-service'
payment_service_path=$workdir/'payment-service'

rm $catalog_service_path/$api_name/*
rm $order_service_path/$api_name/*
rm $payment_service_path/$api_name/*

xargs -n 1 \
  cp $workdir/'api-gateway'/$api_name/*.py \
    <<<"$catalog_service_path/$api_name/ \
	      $order_service_path/$api_name/ \
        $payment_service_path/$api_name/" \
    2>/dev/null

