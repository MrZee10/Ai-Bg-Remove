if [ -z $UPSTREAM_REPO ]
then
  echo "Cloning main Repository"
  git clone https://github.com/MrZee10/Ai-Bg-Remove.git /Ai-Bg-Remove
else
  echo "Cloning Custom Repo from $UPSTREAM_REPO "
  git clone $UPSTREAM_REPO /Ai-Bg-Remove
fi
cd /Ai-Bg-Remove
pip3 install -U -r requirements.txt
echo "Starting ai...🔥"
python3 bot.py
