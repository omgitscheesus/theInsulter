from utils.controller import insulter
from utils.input import insult_in
from utils.output import select_out

prison = True
in_method = 'file'
out_method = 'shell'
input_location = 'insults'
output_location = 'output'
while prison:
    select_out(insulter.insulter(insult_in(in_method, input_location)), out_method, output_location)
    checker = input('Are you crying now? Shall I stop insulting you?')
    if checker == 'have mercy':
        prison = False
