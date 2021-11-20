from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from pinterest_app.models import Board, User, Pin
from .serializers import BoardSerializer, UserSerializer, PinSerializer
from rest_framework import serializers
from . import serializers as ser


@api_view(['GET'])
def board_list(request):
    boards = Board.objects.all()
    ser = BoardSerializer(instance=boards, many=True)
    return Response(data=ser.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def board_detail(request, id):
    response = {}
    board_obj = Board.objects.filter(pk=id)
    if board_obj.exists():
        board_obj = board_obj.first()
        ser = BoardSerializer(instance=board_obj)

        response['data'] = ser.data
        response['status'] = status.HTTP_200_OK
    else:
        response['data'] = {'message': 'failed Movie does not exist'}
        response['status'] = status.HTTP_400_BAD_REQUEST

    return Response(**response)


@api_view(['POST'])
def board_create(request):
    ser = BoardSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
    else:
        return Response(data=ser.errors, status=status.HTTP_400_BAD_REQUEST)

    data = {
        'message': 'success',
        'data': {'id': ser.data.get('id')}

    }

    return Response(data=data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def board_delete(request, id):
    response = {}
    try:
        board_obj = Board.objects.get(pk=id)
        board_obj.delete()
        response['data'] = {'message': 'Successfully Deleted Movie'}
        response['status'] = status.HTTP_200_OK
    except Exception as e:
        response['data'] = {'message': 'Error While Deleting Movie {}'.format(str(e))}
        response['status'] = status.HTTP_400_BAD_REQUEST

    print("Result -> ", response)

    return Response(**response)


@api_view(['PUT', 'PATCH'])
def board_update(request, id):
    try:
        board = Board.objects.get(pk=id)
    except Exception as e:
        return Response(data={'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        ser = BoardSerializer(instance=board, data=request.data)
    elif request.method == 'PATCH':
        ser = BoardSerializer(instance=board, data=request.data, partial=True)

    if ser.is_valid():
        ser.save()
        return Response(data=ser.data, status=status.HTTP_200_OK)

    return Response(data=ser.errors, status=status.HTTP_400_BAD_REQUEST)



#handling password showing *
@api_view(['GET'])
def users_list(request):
    users = User.objects.all()
    ser = UserSerializer(instance=users, many=True)
    return Response(data=ser.data, status=status.HTTP_200_OK)

#
@api_view(['GET'])
def user_detail(request, id):
    response = {}
    user_obj = User.objects.filter(pk=id)
    if user_obj.exists():
        user_obj = user_obj.first()
        ser = UserSerializer(instance=user_obj)

        response['data'] = ser.data
        response['status'] = status.HTTP_200_OK
    else:
        response['data'] = {'message': 'failed User does not exist'}
        response['status'] = status.HTTP_400_BAD_REQUEST

    return Response(**response)



#bin
@api_view(['GET'])
def pin_list(request):
    pins = Pin.objects.all()
    ser = PinSerializer(instance=pins, many=True)
    return Response(data=ser.data, status=status.HTTP_200_OK)


@api_view(['GET'])
def pin_detail(request, id):
    response = {}
    pin_obj = Pin.objects.filter(pk=id)
    if pin_obj.exists():
        pin_obj = pin_obj.first()
        ser = BoardSerializer(instance=pin_obj)

        response['data'] = ser.data
        response['status'] = status.HTTP_200_OK
    else:
        response['data'] = {'message': 'failed Movie does not exist'}
        response['status'] = status.HTTP_400_BAD_REQUEST

    return Response(**response)


@api_view(['POST'])
def pin_create(request):
    ser = PinSerializer(data=request.data)
    if ser.is_valid():
        ser.save()
    else:
        return Response(data=ser.errors, status=status.HTTP_400_BAD_REQUEST)

    data = {
        'message': 'success',
        'data': {'id': ser.data.get('id')}

    }

    return Response(data=data, status=status.HTTP_201_CREATED)


@api_view(['DELETE'])
def pin_delete(request, id):
    response = {}
    try:
        pin_obj = Pin.objects.get(pk=id)
        pin_obj.delete()
        response['data'] = {'message': 'Successfully Deleted Movie'}
        response['status'] = status.HTTP_200_OK
    except Exception as e:
        response['data'] = {'message': 'Error While Deleting Movie {}'.format(str(e))}
        response['status'] = status.HTTP_400_BAD_REQUEST

    print("Result -> ", response)

    return Response(**response)


@api_view(['PUT', 'PATCH'])
def pin_update(request, id):
    try:
        pin = Pin.objects.get(pk=id)
    except Exception as e:
        return Response(data={'message': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'PUT':
        ser = PinSerializer(instance=pin, data=request.data)
    elif request.method == 'PATCH':
        ser = BoardSerializer(instance=pin, data=request.data, partial=True)

    if ser.is_valid():
        ser.save()
        return Response(data=ser.data, status=status.HTTP_200_OK)

    return Response(data=ser.errors, status=status.HTTP_400_BAD_REQUEST)