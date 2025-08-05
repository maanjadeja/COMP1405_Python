def main():

	# only two variables are needed for this "simulation"
	#  - day, which (in a way) is used to record the amount of time elapsed
	#  - lilies, which records the "state" of the pond (i.e., lily coverage)
	day = 1
	lilies = 1

	# my choice was a precondition loop, because it is conceivable (to me) that I
	# may have specified an initial lily coverage where the "answer" is actually
	# "you must remove the lilies immediately", and this would mean that the "body"
	# of the loop wouldn't actually need to be executed at all...
	while lilies < 80:
	
		# although not strictly necessary, simulations often allow the users to
		# "perceive" the passage of time and corresponding changes to the model
		print(f"On day {day} the lily population is at {lilies}%.")
		
		# as the day increases by one, the lily coverage doubles
		lilies *= 2
		day += 1
		
	# after the loop has terminated, the day variable contains the day that the 
	# simulation observed the termination condition, so this is the user's "answer"
	print(f"Remove them any time before day {day}.")


main()