import sys
import antigravity

def my_var():
	if (len(sys.argv) == 4):
		try:
			lat = float(sys.argv[1])
		except:
			return print("latitude should be float type")
		try:
			lon = float(sys.argv[2])
		except:
			return print("longitude should be float type")
		try:
			encrypt = sys.argv[3].encode('utf-8')
		except:
			return print("last argument should be string type")
		antigravity.geohash(lat, lon, encrypt)
	else:
		print("Wrong number of arguments (3 required)")


if __name__ == '__main__':
    my_var()
