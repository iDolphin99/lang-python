'''
Lab : 상속 예제 
'''


# 일반적인 운송수단을 나타내는 클래스이다. 
class Vehicle :                 # 부모 클래스 
    def __init__(self, make, model, color, price):
        self.make = make        # 메이커
        self.model = model      # 모델 
        self.color = color      # 자동차의 색상
        self.price = price      # 자동차의 가격 
        
    def setMake(self,make) :    # 설정자 메서드 
        self.make = make
        
    def getMake(self) :         # 접근자 메서드
        return self.make 
    
    # 차량에 대한 정보를 문자열로 요약하여서 반환한다. 
    def getDesc(self) : 
        return "차량 = (" + str(self.make) + "," + str(self.model) + "," + str(self.color) + "," + str(self.price) + ")"

class Truck(Vehicle) :          # 자식 클래스(부모 클래스)
    def __init__(self, make, model, color, price, payload): # field, method 모두 물려 받음 
        super().__init__(make, model, color, price)         # super -> 부모 객체를 가리킴
        self.payload = payload
    
    def setPayload(self, payload) : # 설정자 메서드, 자식 클래스에서 추가된 메서드 
        self.payload = payload
    
    def getPayload(self) :          # 접근자 메서드
        return self.payload
    
    #def getDesc(self):
    #    return super().getDesc() + str(self.payload)
    
    
def main() : # main 함수 정의 
    myTruck = Truck("Tisla", "Model S", "white", 10000, 2000) # 생성자 super.__init__ 호출 
    myTruck.setMake("Tesla")
    myTruck.setPayload(20000)
    print(myTruck.getDesc())
    
main()