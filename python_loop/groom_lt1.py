# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import numpy as np
import math

input_l = []
while True:
	user_input = int(input(''))
	input_l.append(user_input)

	if len(input_l[1:]) == input_l[0]:
		#user_input = user_input.split('\n')
		cnt_input = []
		for i in range(1, len(input_l)):
			if np.sqrt(input_l[i])-math.isqrt(input_l[i]) == 0:
				cnt_input.append(input_l[i])
			else:
				pass
		break

	else:
		next
		
print(len(cnt_input))

