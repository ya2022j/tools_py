
https://pe-bank.jp/project/python/12038-34/#





for i1,i2 in zip(v_name,links):
	f_name = "".join(i1.split())
	urllib.request.urlretrieve(i2, '{0}/{1}.mp4'.format(fpic_path,f_name[:20]))
	# Fname = fpic_path+"/"+"".join(i1.split())

	# cmd = 'wget -P {0} {1}.mp4'.format(Fname, i2)
	# subprocess.call(cmd, shell=True)

	# print(cmd)