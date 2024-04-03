#import this
import random


def choose_options():
  options = ('piedra', 'papel', 'tijera')

  user_option = input('piedra, papel o tijera => ').lower()
  if user_option not in options:
    print('Esa opcion no existe')
    # continue
    return None, None

  computer_option = random.choice(options)

  return user_option, computer_option


def check_rules(user_option, computer_option, score_player, score_computer):

  if user_option == computer_option:
    print('¡Empate!')
    print(f'Puntaje => User: {score_player} vs Computer: {score_computer}')
  elif user_option == 'piedra':
    if computer_option == 'tijera':
      score_player += 1
      print('Piedra le gana a la tijera')
      print('¡User Ganó!')
      print(f'Puntaje => User: {score_player} vs Computer: {score_computer}')
    else:
      score_computer += 1
      print('Papel le gana a la piedra')
      print('Computer Ganó')
      print(f'Puntaje => User: {score_player} vs Computer: {score_computer}')
  elif user_option == 'papel':
    if computer_option == 'piedra':
      score_player += 1
      print('Papel le gana a la piedra')
      print('¡User Ganó!')
      print(f'Puntaje => User: {score_player} vs Computer: {score_computer}')
    else:
      score_computer += 1
      print('Tijera le gana a la papel')
      print('¡Computer Ganó!')
      print(f'Puntaje => User: {score_player} vs Computer: {score_computer}')
  elif user_option == 'tijera':
    if computer_option == 'papel':
      score_player += 1
      print('Tijera le gana a la papel')
      print('¡User Ganó!')
      print(f'Puntaje => User: {score_player} vs Computer: {score_computer}')
    else:
      score_computer += 1
      print('Piedra le gana a la tijera')
      print('Computer Ganó')
      print(f'Puntaje => User: {score_player} vs Computer: {score_computer}')

  return score_player, score_computer


def check_winner(score_player, score_computer):
  if score_player == 3 and score_computer < 3:
    #break
    print(f'Ganó el usuario {score_player} vs {score_computer}')

  if score_computer == 3 and score_player < 3:

    print(f'Ganó el usuario {score_player} vs {score_computer}')


def run_game():

  roundTotal = 3
  score_player = 0
  score_computer = 0
  if (roundTotal == 3 and (score_player and score_player == 2)):
    print(f'------ Round {roundTotal + 1} ------')
    user_option, computer_option = choose_options()
    score_player, score_computer = check_rules(user_option, computer_option, score_player, score_computer)

    check_winner(score_player, score_computer)
  else:

    for round in range(1, roundTotal + 1):

      print(roundTotal)
      if score_player or score_computer < 3:
        print(f'------ Round {round} ------')

        user_option, computer_option = choose_options()
        score_player, score_computer = check_rules(user_option, computer_option, score_player, score_computer)
        roundTotal += 1
      continue

    check_winner(score_player, score_computer)


run_game()