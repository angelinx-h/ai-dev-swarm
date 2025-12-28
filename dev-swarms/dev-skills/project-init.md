Please check `dev-swarms/docs/software-dev-classification.md` and update `dev-swarms/docs/repository-structure.md`

1. for different scale project, we need different stages, and for each stage, we need to create different docs
2. check the docs file under each stage, we need to have a max docs file list to meet the large scale project in each stage
3. you can add/merge/split/remove any files under each stage, 
4. each file needs to have a short comment to explain what it is for
5. for very small project, we may just need 

```
00-init-ideas/
  README.md  # for how to immplement the code `src/script_name.sh` or the refined requirement
src/
  script_name.sh
```

Do not update folder for 

09-sprints/ 
99-archive/ 
features/     
src/

As they are for special use
Do not split the structure for different level project, we need to have a max file list for each stage