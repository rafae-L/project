from settings import *
from vec_and_scal_proizvedenie import *

class wall():
    def __init__(self, x, y, x1, y1, ax, ay, type = 1, h = 50):
        #начальная позиция
        self.position_0 = [x, y]
        self.position = [x, y]

        #конечная позиция
        self.endsition_0 = [x1, y1]
        self.endsition = [x1, y1]

        #нормаль
        self.n = [n1, n2]
        self.a = [x1 - x, y1 - y]

        '''
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        ЗАПИСЫВАТЬ ВЕРШИНЫ НАДО ТАК, ЧТОБЫ ax > 0
        !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
        '''

        self.k_for_a = (x1 - x)**2 + (y1 - y)**2
        self.edenich_a = a / k_for_a**0.5
        

        #тип стены (пока что только один)
        '''
        1 - литая стена, постоянной высоты h    
        '''
        self.type = 1
        self.h = 50

        self.rho

    def in_view(self, obj)
        a1 = [self.position[0] - obj.x, self.position[1] - obj.y]
        a2 = [self.endsition[0] - obj.x, self.endsition[1] - obj.y]

        p1_max = vectornoe(a1, obj.a_max)
        p1_min = vectornoe(a1, obj.a_min)
        p2_max = vectornoe(a2, obj.a_max)
        p2_min = vectornoe(a2, obj.a_min)

        #проверка на наличие части стены между векторами обзора
        if(p1_max * p1_min == -1):
            if(p2_max == -1):
                #меняем конечные координаты стен, на те, которые находятся в угле видимости
                t = (a2[0] * self.a[1] - a2[1] * self.a[0]) / (obj.a_max[0] * self.a[1] - obj.a_max[1] * self.a[0])
                self.endsition = [obj.x + obj.a_max[0] * t, obj.y + obj.a_max[1] * t]

                a2 = [obj.a_max[0] * t, obj.a_max[1] * t]

            elif(p2_min == 1):
                t = (a2[0] * self.a[1] - a2[1] * self.a[0]) / (obj.a_min[0] * self.a[1] - obj.a_min[1] * self.a[0])
                self.endsition = [obj.x + obj.a_min[0] * t, obj.y + obj.a_min[1] * t]

                a2 = [obj.a_min[0] * t, obj.a_min[1] * t]

            else:
                return 0
        

        elif(p2_max * p2_min == -1):
            if(p1_max == -1):
                t = (a1[0] * self.a[1] - a1[1] * self.a[0]) / (obj.a_max[0] * self.a[1] - obj.a_max[1] * self.a[0])
                self.position = [obj.x + obj.a_max[0] * t, obj.y + obj.a_max[1] * t]

                a1 = [obj.a_max[0] * t, obj.a_max[1] * t]

            elif(p1_min == 1):
                t = (a1[0] * self.a[1] - a1[1] * self.a[0]) / (obj.a_min[0] * self.a[1] - obj.a_min[1] * self.a[0])
                self.position = [obj.x + obj.a_min[0] * t, obj.y + obj.a_min[1] * t]

                a1 = [obj.a_min[0] * t, obj.a_min[1] * t]

            else:
                return 0
            
        
        elif(p1_max <= 0):
            if(vectornoe(a1, a2) == -1):
                #p1_max == -1
                t = (a1[0] * self.a[1] - a1[1] * self.a[0]) / (obj.a_max[0] * self.a[1] - obj.a_max[1] * self.a[0])
                self.position = [obj.x + obj.a_max[0] * t, obj.y + obj.a_max[1] * t]
                a1 = [obj.a_max[0] * t, obj.a_max[1] * t]

                #p2_min == 1
                t = (a2[0] * self.a[1] - a2[1] * self.a[0]) / (obj.a_min[0] * self.a[1] - obj.a_min[1] * self.a[0])
                self.endsition = [obj.x + obj.a_min[0] * t, obj.y + obj.a_min[1] * t]
                a2 = [obj.a_min[0] * t, obj.a_min[1] * t]

            else:
                return 0

        elif(p1_min >= 0)
            if(vectornoe(a1, a2) == 1):
                #p1_min == 1
                t = (a1[0] * self.a[1] - a1[1] * self.a[0]) / (obj.a_min[0] * self.a[1] - obj.a_min[1] * self.a[0])
                self.position = [obj.x + obj.a_min[0] * t, obj.y + obj.a_min[1] * t]
                a1 = [obj.a_min[0] * t, obj.a_min[1] * t]

                #p2_max == -1
                t = (a2[0] * self.a[1] - a2[1] * self.a[0]) / (obj.a_max[0] * self.a[1] - obj.a_max[1] * self.a[0])
                self.endsition = [obj.x + obj.a_max[0] * t, obj.y + obj.a_max[1] * t]
                a2 = [obj.a_max[0] * t, obj.a_max[1] * t]

            else:
                return 0


        else:
            return 0

        #проверка, находится ли стенка на растоянии меньшем чем view_dist
        h = skalarnoe(a1, self.n)
        r_a1 = a1[0]**2 + a1[1]**2
        r_a2 = a2[0]**2 + a2[1]**2

        if(vectornoe(a1, self.n) != vectornoe(a2, self.n)):
            if((-obj.view_dist <= h) and (h <= obj.view_dist)):
                p1 = (h**2 - r_a1) / scalarnoe(a1, self.a)
                p2 = (h**2 - r_a2) / scalarnoe(a2, self.a)

                if(obj.view_dist**2 - h**2 < p1**2 * self.k_for_a):
                    a1 = h * n - (obj.view_dist**2 - h**2)**0.5 * self.edenich_a
                    self.position = [obj.x + a1[0], obj.y + a1[1]]

                if(obj.view_dist**2 - h**2 < p2**2 * self.k_for_a):
                    a2 = h * n + (obj.view_dist**2 - h**2)**0.5 * self.edenich_a
                    self.endsition =  [obj.x + a2[0], obj.y + a2[1]]
                
            

        elif(r_a1 <= obj.view_dist**2):
            p = (h**2 - r_a1) / scalarnoe(a1, self.a)

            new_a2 = a1 + p * self.a + (obj.view_dist**2 - h**2)**0.5 * self.edenich_a
            if(new_a2[0] < a2[0])
                a2 = new_a2
                self.endsition = [obj.x + new_a2[0], obj.y + new_a2[1]]


        elif(r_a2 <= obj.view_dist**2):
            p = (h**2 - r_a2) / scalarnoe(a2, self.a)

            a1 = a2 + p * self.a + (obj.view_dist**2 - h**2)**0.5 * self.edenich_a
            self.position = [obj.x + a1[0], obj.y + a1[1]]
        

        else:
            return 0
        
    
    
