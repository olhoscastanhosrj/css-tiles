#coding: utf-8
block_width  = 33.333333333 / 3
block_height = 33.333333333 / 3
for x in range(0,3):
	for y in range(0,3):
		top    = y * 33.333333333
		left   = x * 33.333333333
		#width == small
		print ".tile-%i-%i-small{position:absolute;top:%02.8f%%;left:%2.8f%%;width:%02.8f%%;height:%02.8f%%}" 		       %(x + 1 ,y + 1,left,top,(block_width * 1.),(block_height * 1.))
		print ".tile-%i-%i-small *{padding: 0%%;margin: 0%%}"  %(x + 1 ,y + 1)
		print ".tile-%i-%i-small div{position:relative}"  %(x + 1 ,y + 1)
		print ".tile-%i-%i-small-vertical-medium{position:absolute;top:%2.8f%%;left:%02.8f%%;width:%02.8f%%;height:%02.8f%%}"  %(x + 1 ,y + 1,left,top,(block_width * 1.),(block_height * 2.))
		print ".tile-%i-%i-small-vertical-medium *{padding: 0%%;margin: 0%%}"  %(x + 1 ,y + 1)
		print ".tile-%i-%i-small-vertical-medium div{position:relative}"  %(x + 1 ,y + 1)		
		print ".tile-%i-%i-small-vertical-large{position:absolute;top:%2.8f%%;left:%02.8f%%;width:%02.8f%%;height:%02.8f%%}"   %(x + 1 ,y + 1,left,top,(block_width * 1.),(block_height * 3.))
		print ".tile-%i-%i-small-vertical-large *{padding: 0%%;margin: 0%%}"  %(x + 1 ,y + 1)
		print ".tile-%i-%i-small-vertical-large div{position:relative}"  %(x + 1 ,y + 1)		
		print ".tile-%i-%i-small-vertical-expansible{position:absolute;top:%02.8f%%;left:%2.8f%%;width:%02.8f%%;height:%02.8f%%}"       %(x + 1 ,y + 1,left,top,(block_width * 1.),(block_height * 1.))
		print ".tile-%i-%i-small-vertical-expansible *{padding: 0%%;margin: 0%%}"  %(x + 1 ,y + 1)
		print ".tile-%i-%i-small-vertical-expansible div{position:relative}"  %(x + 1 ,y + 1)		
		print ".tile-%i-%i-small-vertical-expansible:hover{position:absolute;top:%02.8f%%;left:%2.8f%%;width:%02.8f%%;height:%02.8f%%}" %(x + 1 ,y + 1,left,top,(block_width * 1.),(block_height * 2.))
				
		if x <= 3 and y <= 3 and abs(x + y) > 0:
			for sx in range(1, 3 - x):
				for sy in range(1,3 - y):
					print ".tile-%i-%i-small-collapse-%i-%i div{position:relative}"  %(x + 1 ,y + 1,sx, sy)
					print ".tile-%i-%i-small-collapse-%i-%i *{padding: 0%%;margin: 0%%}" %(x + 1 ,y + 1,sx, sy)
					print ".tile-%i-%i-small-collapse-%i-%i{position:absolute;top:%02.8f%%;left:%2.8f%%;width:%02.8f%%;height:%02.8f%%}" %(x + 1 ,y + 1,sx, sy ,left,top,(block_width * 1.)+ (33.333333333 * sx),(block_height * 1.) +  (33.333333333 * sy))
		# width == medium
		print ".tile-%i-%i-medium-vertical-small{position:absolute;top:%02.8f%%;left:%02.8f%%;width:%02.8f%%;height:%02.8f%%}"  %(x + 1 ,y + 1,left,top,(block_width * 2.),(block_height * 1.))
		print ".tile-%i-%i-medium-vertical-small *{padding: 0%%;margin: 0%%}" %(x + 1 ,y + 1)
		print ".tile-%i-%i-medium-vertical-small div{position:relative}"  %(x + 1 ,y + 1)
		print ".tile-%i-%i-medium{position:absolute;top:%02.8f%%;left:%02.8f%%;width:%02.8f%%;height:%02.8f%%}"                 %(x + 1 ,y + 1,left,top,(block_width * 2.),(block_height * 2.))
		print ".tile-%i-%i-medium *{padding: 0%%;margin: 0%%}" %(x + 1 ,y + 1)
		print ".tile-%i-%i-medium div{position:relative}"  %(x + 1 ,y + 1)
		print ".tile-%i-%i-medium-vertical-large{position:absolute;top:%02.8f%%;left:%02.8f%%;width:%02.8f%%;height:%02.8f%%}"  %(x + 1 ,y + 1,left,top,(block_width * 2.),(block_height * 3.))
		print ".tile-%i-%i-medium-vertical-large *{padding: 0%%;margin: 0%%}"  %(x + 1 ,y + 1)
		print ".tile-%i-%i-medium-vertical-large div{position:relative}"  %(x + 1 ,y + 1)		
		print ".tile-%i-%i-medium-vertical-expansible{position:absolute;top:%02.8f%%;left:%2.8f%%;width:%02.8f%%;height:%02.8f%%}"       %(x + 1 ,y + 1,left,top,(block_width * 1.),(block_height * 2.))
		print ".tile-%i-%i-medium-vertical-expansible *{padding: 0%%;margin: 0%%}"  %(x + 1 ,y + 1)
		print ".tile-%i-%i-medium-vertical-expansible div{position:relative}"  %(x + 1 ,y + 1)
		print ".tile-%i-%i-medium-vertical-expansible:hover{position:absolute;top:%02.8f%%;left:%2.8f%%;width:%02.8f%%;height:%02.8f%%}" %(x + 1 ,y + 1,left,top,(block_width * 1.),(block_height * 3.))

		if x <= 3 and y <= 3 and abs(x + y) > 0:
			for sx in range(1, 3 - x):
				for sy in range(1,3 - y):
					print ".tile-%i-%i-medium-collapse-%i-%i div{position:relative}"  %(x + 1 ,y + 1,sx, sy)
					print ".tile-%i-%i-medium-collapse-%i-%i *{padding: 0%%;margin: 0%%}"  %(x + 1 ,y + 1,sx, sy)
					print ".tile-%i-%i-medium-collapse-%i-%i{position:absolute;top:%02.8f%%;left:%2.8f%%;width:%02.8f%%;height:%02.8f%%}" %(x + 1 ,y + 1,sx, sy,left,top,(block_width * 2.) + (33.333333333 * sx),(block_height * 2.) +  (33.333333333 * sy))
		#width == large	
		print ".tile-%i-%i-large-vertical-small{position:absolute;top:%02.8f%%;left:%02.8f%%;width:%02.8f%%;height:%02.8f%%}"   %(x + 1 ,y + 1,left,top,(block_width * 3. ),(block_height * 1.))
		print ".tile-%i-%i-large-vertical-small *{padding: 0%%;margin: 0%%}"  %(x + 1 ,y + 1)
		print ".tile-%i-%i-large-vertical-small div{position:relative}"  %(x + 1 ,y + 1)
		print ".tile-%i-%i-large-vertical-medium{position:absolute;top:%02.8f%%;left:%02.8f%%;width:%02.8f%%;height:%02.8f%%}"  %(x + 1 ,y + 1,left,top,(block_width * 3. ),(block_height * 2.))
		print ".tile-%i-%i-large-vertical-medium *{padding: 0%%;margin: 0%%}" %(x + 1 ,y + 1)
		print ".tile-%i-%i-large-vertical-medium div{position:relative}"  %(x + 1 ,y + 1)
		print ".tile-%i-%i-large{position:absolute;top:%02.8f%%;left:%02.8f%%;width:%02.8f%%;height:%02.8f%%}"                  %(x + 1 ,y + 1,left,top,(block_width * 3. ),(block_height * 3.))
		print ".tile-%i-%i-large div{position:relative}"  %(x + 1 ,y + 1)		
		print ".tile-%i-%i-large *{padding: 0%%;margin: 0%%}" %(x + 1 ,y + 1)
