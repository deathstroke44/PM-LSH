dataset_infos=[('enron', 94987, 200, 200, 1369, 20), ('lendb', 1000000, 100, 100, 256, 100), ('deep', 1000000, 200, 200, 256, 20), ('geofon', 275174, 100, 100, 128, 100), ('tiny5m', 5000000, 1000, 1000, 384, 100), ('crawl', 1989995, 10000, 10000, 300, 100), ('netflix', 17770, 1000, 1000, 300, 100), ('glove', 1192514, 200, 200, 100, 20), ('sun', 79106, 200, 200, 512, 20), ('audio', 53387, 200, 200, 192, 20), ('cifar', 50000, 200, 200, 512, 20), ('instancegm', 1000000, 100, 100, 128, 100), ('random', 1000000, 200, 200, 100, 20), ('OBST2024', 1000000, 300, 300, 256, 100), ('word2vec', 1000000, 1000, 1000, 300, 100), ('millionSong', 992272, 200, 200, 420, 20), ('Meier2019JGR', 1000000, 300, 300, 256, 100), ('nuswide', 268643, 200, 200, 500, 20), ('ethz', 36643, 100, 100, 256, 100), ('Music', 1000000, 100, 100, 100, 100), ('ISC_EHB_DepthPhases', 1000000, 300, 300, 256, 100), ('MNIST', 69000, 200, 200, 784, 20), ('space1V', 1000000, 100, 100, 100, 100), ('vcseis', 160178, 100, 100, 256, 100), ('OBS', 1000000, 300, 300, 256, 100), ('sald1m', 1000000, 100, 100, 128, 100), ('nytimes', 290000, 100, 100, 256, 100), ('text-to-image', 1000000, 100, 100, 200, 100), ('movielens', 10677, 1000, 1000, 150, 100), ('yahoomusic', 136736, 100, 100, 300, 100), ('seismic1m', 1000000, 100, 100, 256, 100), ('siftsmall', 10000, 100, 100, 128, 100), ('NEIC', 1000000, 300, 300, 256, 100), ('Iquique', 578853, 300, 300, 256, 100), ('PNW', 1000000, 300, 300, 256, 100), ('bigann', 1000000, 100, 100, 128, 100), ('lastfm', 292385, 100, 100, 65, 100), ('txed', 519589, 100, 100, 256, 100), ('stead', 1000000, 100, 100, 256, 100), ('gist', 1000000, 1000, 1000, 960, 100), ('trevi', 99900, 200, 200, 4096, 20), ('notre', 332668, 200, 200, 128, 20), ('uqv', 1000000, 10000, 10000, 256, 100), ('sift', 1000000, 10000, 10000, 128, 100), ('imageNet', 2340373, 200, 200, 150, 20), ('ukbench', 1097907, 200, 200, 128, 20), ('astro1m', 1000000, 100, 100, 256, 100), ('Yelp', 77079, 100, 100, 50, 100)]

excludes=['crawl','gist','tiny5m','enron',]



import sys
final_run=''
content=open("big-script-template-1.sh", "r").read()
for info in dataset_infos:
    ds=info[0]
    n=str(info[1])
    d=str(info[2])
    qn=str(info[3])
    if not (ds in excludes):
        log_file_name = ds+".sh"
        final_run=final_run+'bash '+log_file_name+' & '
        sys.stdout = open(log_file_name, "w")
        new_content=content+''
        new_content=new_content.replace('[N]',n)
        new_content=new_content.replace('[dim]',d)
        new_content=new_content.replace('[K]','100')
        new_content=new_content.replace('[dataset]',ds)
        print(new_content)
final_run=final_run+'echo 1'
sys.stdout = open('run_all.sh', "w")          
print(final_run)           
    
    
