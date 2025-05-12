from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import PicoPlacaRequestSerializer, PicoPlacaResponseSerializer
from .services    import PicoPlacaPredictor

class PicoPlacaAPIView(APIView):
    """
    POST /api/pico_placa/
    { plate: str, date: "YYYY-MM-DD", time: "HH:MM" }
    → { can_drive: bool }
    """
    def post(self, request):
        req_ser = PicoPlacaRequestSerializer(data=request.data)
        req_ser.is_valid(raise_exception=True)
        data = req_ser.validated_data

        predictor = PicoPlacaPredictor(
            plate     = data['plate'],
            date_str  = data['date'].isoformat(),
            time_str  = data['time'].strftime('%H:%M'),
        )
        allowed = predictor.can_drive()

        resp_ser = PicoPlacaResponseSerializer({'can_drive': allowed})
        return Response(resp_ser.data, status=status.HTTP_200_OK)

