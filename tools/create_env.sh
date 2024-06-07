
set -e
# deactivate
module purge
module load  StdEnv/2020 python/3.10.2
module load gcc/9.3.0 opencv/4.8.0 cuda/11.7
echo "loading module done"

echo "Creating new virtualenv"

virtualenv ../env/$1
source ../env/$1/bin/activate

echo "Activating virtual env"

cd ../

pip install mmengine>=0.8.3
pip install mmcv
pip install -v -e .

echo "Installing requirements"
pip install -r requirements.txt