from .apps import ApiConfig
from rest_framework.views import APIView
from rest_framework.response import Response
#import necessary libraries




class Prediction(APIView):
    def post(self, request):
        data = request.data
        model = ApiConfig.model
        value = [[data['EnvironmentSatisfaction'],data['JobSatisfaction'],data['WorkLifeBalance'],data['Age'],data['BusinessTravel'],data['Department'],data['DistanceFromHome'],data['Education'],data['Gender'],data['JobLevel'],data['JobRole'],data['MaritalStatus'],data['MonthlyIncome'],data['NumCompaniesWorked'],data['PercentSalaryHike'],data['TotalWorkingYears'],data['YearsAtCompany'],data['YearsSinceLastPromotion'],data['YearsWithCurrManager'],data['JobInvolvement'],data['PerformanceRating']]]
        
        predicted = model.predict(value)[0]
        response_dict = {"result": predicted}
        return Response(response_dict, status=200)