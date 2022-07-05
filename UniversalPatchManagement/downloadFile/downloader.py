import requests 
import sys, time

def Download_file(url):
    local_filename = url.split('/')[-1]
    # NOTE the stream=True parameter below
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        total_length = int(r.headers.get('content-length'))
        with open(local_filename, 'wb') as f:
            chunk_size=8192
            for i, chunk in enumerate(r.iter_content(chunk_size=chunk_size)):
                # If you have chunk encoded response uncomment if
                # and set chunk_size parameter to None.
                #if chunk: 
                c = i * chunk_size / total_length * 100
                f.write(chunk)
                sys.stdout.write(f" Downloaded from {url} \r{round(c,2)}%")
                #time.sleep(.1)
                sys.stdout.flush()

    return local_filename

