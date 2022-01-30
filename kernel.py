from dictionary import *
import subprocess


def runcommand(command=[],timeout="5",stdIN=b""):
	#command[:0] = ["timeout",timeout]
	proc = subprocess.Popen(command, bufsize=0, stdout=subprocess.PIPE)
	std_out, std_err = proc.communicate(input=b''+stdIN)
	#if proc.returncode == 124:
	#	print("timeout")
	#elif proc.returncode == 0 or proc.returncode == 3:
	#	print("ok")
	#else:
	#	print(proc.returncode)
	#	print("error")
	proc.kill()
	return std_out, std_err



def main():
	alphabet = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z", "0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
	for password in generateur_recurrent_d_espace(alphabet, "", 5):
		print(password)
		std_out, std_err = runcommand(["python3", "password.py", password])
		if std_out == b'0\n':
			print("The password is:" + password)
			exit()


if __name__ == '__main__':
	main()