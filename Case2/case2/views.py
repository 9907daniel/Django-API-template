from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
import boto3


@api_view(['GET', 'POST'])
def tests(request):
    db = boto3.resource('dynamodb')
    table = db.Table('test')
    if request.method == 'GET':
        test_data = table.scan()
        return Response({'test': test_data.get('Items')})
    elif request.method == 'POST':
        try:
            table.put_item(Item=request.data)
            return Response(status=status.HTTP_201_CREATED)
        except Exception:
            return Response({'error': 'Failed to insert'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
def test(request, name):
    db = boto3.resource('dynamodb')
    table = db.Table('test')
    if request.method == 'GET':
        test = table.get_item(Key={
            'name': name
        })

        if (test.get('Item') is not None):
            return Response({'test': test.get('Item')})
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        try:
            table.put_item(Item=request.data)
            return Response(status=status.HTTP_200_OK)
        except Exception:
            return Response({'error': 'Failed to update'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    if request.method == 'DELETE':
        table.delete_item(Key={
            'name': name
        })
        return Response(status=status.HTTP_200_OK)


@api_view(['GET', 'POST'])
def work_orders(request):
    db = boto3.resource('dynamodb')
    table = db.Table('work_order')
    if request.method == 'GET':
        work_order_data = table.scan()
        return Response({'work_order': work_order_data.get('Items')})
    elif request.method == 'POST':
        try:
            table.put_item(Item=request.data)
            return Response(status=status.HTTP_201_CREATED)
        except Exception:
            return Response({'error': 'Failed to insert'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(['GET', 'PUT', 'DELETE'])
def work_order(request, name):
    db = boto3.resource('dynamodb')
    table = db.Table('work_order')
    if request.method == 'GET':
        work_order = table.get_item(Key={
            'name': name
        })

        if (work_order.get('Item') is not None):
            return Response({'work_order': work_order.get('Item')})
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'PUT':
        try:
            table.put_item(Item=request.data)
            return Response(status=status.HTTP_200_OK)
        except Exception:
            return Response({'error': 'Failed to update'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    if request.method == 'DELETE':
        table.delete_item(Key={
            'name': name
        })
        return Response(status=status.HTTP_200_OK)
