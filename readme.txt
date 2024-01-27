Description: Different people want to generate an xml rss data file from their podcasts in yml format.

1. Repo: podcast-test
  a. Action: .github/workflows/main.yml (waits for podcast data file 'feed.yml' to change; ie. pushed change onto branch)
     I. If branch push, run: 
	      # calls username/repositoryWithAciton@branch
        jackfobel/podcast-generator@main # calls another repository and executes action in the root.
3. Repo: podcast-generator
   a. Action:  action.yml (doesn't go in workflows folder)
      I.   Runs the Dockerfile to start up the vm.
      II.  Dockerfile runs the entrypoint.sh file
      III. Entrypoint.sh runs the feed.py file to create the podcast.xml rss data feed file in
	     the calling repository (podcast-test)
