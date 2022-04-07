import pygame


#Colors
red = (255,0,0)
green = (0, 255, 0)
purple = (255,0,255)
black = (0,0,0)
white = (255,255,255)
pygame.init()
width, height = 800,  600
backgroundColor = (0,  0,  0)


fontObjMain = pygame.font.Font('Games.ttf', 60)
fontObjMenu = pygame.font.Font('Games.ttf', 30)

screen = pygame.display.set_mode((width, height))
icon = pygame.image.load('giphy.gif')
pygame.display.set_icon(icon)



screen.fill(backgroundColor)

#title
title_font = fontObjMain
title = title_font.render('Snake Leg Pool!', False,white)
titleRect = title.get_rect()
titleRect.center = (width//2 , 50)
screen.blit(title, titleRect)

#High Scores
main_font = fontObjMenu
highScores = main_font.render('High Scores',False,white)
highRect = highScores.get_rect()
highRect.center = (width-600 ,height-200)
screen.blit(highScores, highRect)

#high scores using dictionary
high_scores = {"name1": 10, "name2": 9, "name3": 8, "name4": 7, 
              "name5": 6, "name6": 5}

# kind of useless because we can print a dict
def get_high_scores (high_scores):
  scores = high_scores.keys()
  return scores

def update_high_scores(high_scores_dict, current_score):
  lowest_current_key = min(high_scores_dict, key=high_scores_dict.get)
  lowest_current_value = high_scores_dict[lowest_current_key]

  if (lowest_current_value < current_score):
    print("NEW HIGHSCORE!")
    user_name = input(print("Enter your name"))
  new_score_dict = {user_name: current_score}
  del high_scores_dict[lowest_current_key]
  high_scores_dict.update(new_score_dict)
  
#Play Game
# Need to add functionality to start game
play = main_font.render('Play Game',False,white)
playRect = play.get_rect()
playRect.center = (width-200,height-200)
screen.blit(play, playRect)

#Display  Credits
# Need to add functionality to display the credits
credits = main_font.render('Credits: 0',False,white) #load credits on this line
creditsRect = credits.get_rect()
creditsRect.center = (width//2 ,height-150)
screen.blit(credits, creditsRect)





# display logo
icon_sized = pygame.transform.scale(icon,(350,235))
screen.blit(icon_sized, (200,130))




pygame.display.flip()


pygame.display.update()



def startGame(credits):
  high_scores = {"name1": 10, "name2": 9, "name3": 8, "name4": 7, 
              "name5": 6, "name6": 5}
  currentScore = 0
  sensorReading = 0
  print("You have " + str(credits) + " credit(s)")
  currentBalls = credits * 3
  print("You have " + str(currentBalls) + " shots")
  for i in range(currentBalls):
    print("Take shot number " + str(i + 1))
    sensorReading = input("Input sensor of where ball went: ")
    if(sensorReading == "1"):
      currentScore+=500
      print("You scored 500 points")
      print("Your current score is: " + str(currentScore))
    if(sensorReading == "2"):
      currentScore+=1000
      print("You scored 1000 points")
      print("Your current score is: " + str(currentScore))
    if(sensorReading == "3"):
      currentScore+=2000
      print("You scored 2000 points")
      print("Your current score is: " + str(currentScore))
    if(sensorReading == "4"):
      currentScore+=3000
      print("You scored 3000 points")
      print("Your current score is: " + str(currentScore))
    if(sensorReading == "5"):
      currentScore+=4000
      print("You scored 4000 points")
      print("Your current score is: " + str(currentScore))
    if(sensorReading == "6"):
      currentScore+=10000
      print("You hit it in the hole! 10000 points")
      print("Your current score is: " + str(currentScore))
    if(sensorReading == "7"):
      currentScore+=5000
      print("You hit it too far 5000 points")
      print("Your current score is: " + str(currentScore))
    print("Final Score: " + str(currentScore))
  ###
  update_high_scores(high_scores, currentScore)
  print("Current HighScores: ", high_scores)

    
  
print("Welcome to Snake Leg Pool")
credits = 0
currentBalls = 0
creditInput = input("Press L or M to enter credit and N to start game: ")
while creditInput != 'N':
  if(creditInput == 'L' or creditInput == 'M'):
    credits+=1
    print("One credit entered")
    creditInput = input("Press L or M to enter credit and N to start game: ")
    
if(creditInput == 'N'):
  startGame(credits)



  
