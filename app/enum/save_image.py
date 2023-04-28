import base64
import io
from io import BytesIO
import matplotlib.pyplot as plt

def Save_image():
  buffer = BytesIO()
  plt.savefig(buffer, format='png')
  graphic_image = base64.b64encode(buffer.getvalue()).decode('utf-8')
  return graphic_image
