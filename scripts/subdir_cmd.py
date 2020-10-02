import os
import json
import fire
import subprocess
import logging

logging.basicConfig(level=logging.DEBUG)

class Meta(object):

    def run_all_metas(self, command, file='.meta'):
        """
        Looks for meta files within the keys of the .meta file that is generated by the meta.yaml. It then runs a supplied command such as meta git clone
        :param command: The command to run in that directory
        :param file: The kind of file to iterate over.
        :return:
        """
        if file in os.listdir("."):
            with open(file, 'r') as f:
                meta_file = json.load(f)
            if file == '.meta':
                for k in meta_file['projects']:
                    # k - key in the .meta file representing the is path
                    if os.path.isfile(os.path.join(k, '.meta')):
                        logging.debug(".meta file found in %s" % k)

                        os.chdir(k)
                        subprocess.call(command, shell=True, stdout=subprocess.PIPE)
                        self.run_all_metas(command)
                    else:
                        logging.debug("No .meta file in %s" % k)

    def clone_all(self):
        self.run_all_metas('meta git clone .')

    def pull_all(self):
        self.run_all_metas('meta git pull .')

    def stash_all(self):
        self.run_all_metas('meta git stash .')

    def stash_apply_all(self):
        self.run_all_metas('meta git stash apply .')

    def status_all(self):
        self.run_all_metas('meta git status -u .')

    def branch_all(self, branch):
        self.run_all_metas('meta git branch -b %s' % branch)

    def add_all(self):
        self.run_all_metas('meta git add * .*')

    def commit_all(self, message=''):
        if not message:
            raise ValueError('Need to supply a message to commit')
        self.run_all_metas('meta git commit -m "%s"' % message)

    def push_all(self, branch=''):
        if not branch:
            raise ValueError('Need to supply a message to commit')
        self.run_all_metas('meta git push origin %s' % branch)


if __name__ == '__main__':
    fire.Fire(Meta(), name='Meta')
