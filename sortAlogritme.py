"""
   x = 0
    y = 300
    bar_width = 10
    bar_height = 200
    bar = pygame.Rect(x,y,bar_width,bar_height)
    color = pygame.Color("green")
    pygame.draw.rect(screen,color,bar)
    pygame.display.flip()
"""


import pygame
import random

# golbal varaibles
width = 600
height = 400
screen = pygame.display.set_mode((width,height))
pygame.init()
n = 50



def draw_bar(array,i,screen,color):
     n = len(array)
     w , h = screen.get_size();
     bar_width = w // n
     bar_height = h // n * array[i] 
     x = bar_width * i 
     y =  h - bar_height  
     bar = pygame.Rect(x,y,bar_width,bar_height)
     pygame.draw.rect(screen,color,bar);   
    
    
def draw_bars(array,screen):
    screen.fill(pygame.Color("black"))   
    n = len(array)
    for i in range(n):
        draw_bar(array,i,screen,pygame.Color("green"));
    pygame.display.flip()

def bubbleSort(arr,screen):
    n = len(arr)
    # For loop to traverse through all 
    # element in an array
    for i in range(n):
        for j in range(0, n - i - 1):
            # Range of the array is from 0 to n-i-1
            # Swap the elements if the element found 
            #is greater than the adjacent element
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            draw_bars(arr,screen);
                
# animation loop 

animating = True
array = random.sample(range(1,n+1),n);    

while animating:
    #   create array 
    
    bubbleSort(array,screen)
     
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            animating = False 
    
    
    
    
