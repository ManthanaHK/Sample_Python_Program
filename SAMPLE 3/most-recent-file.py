import os, datetime,sys

def recentModification(dirpath):
    formatted_times = {}

    files = os.listdir(dirpath)

    for file in files:
        tme = os.path.getmtime(dirpath+"\\"+file)
        timeModifed = datetime.datetime.fromtimestamp(tme)
        formatted_times[timeModifed.strftime("%Y-%m-%d %H:%M:%S")] = dirpath+"\\"+file
    
    recentTime = max(formatted_times.keys())
    print(f"Most Recently modified file is {formatted_times[recentTime]}. The time is {recentTime}")

if len(sys.argv) != 2:
    print("USAGE: python <python file> <folder path>")
else:
    path = sys.argv[1]
    recentModification(path)