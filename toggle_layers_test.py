import sys
import ezdxf

TEST_FILE_PATH = "C:\\Users\\bgonzalez\\Documents\\TEST_FILE.dxf"


#Load the dxf file and store it as doc
try:
    doc = ezdxf.readfile(TEST_FILE_PATH)
    msp = doc.modelspace()
except IOError:
    print("Not a DXF or generic I/O error")
    sys.exit(1)
except ezdxf.DXFStructureError:
    print(f"Invalid or corrupted DXF file.")
    sys.exit(2)


#Check all of the available layers in the doc
for layer in doc.layers:
    layer_name = layer.dxf.name
    
    #turn off the ws layer if it exists
    if layer_name == "WS":
        layer.freeze()
        print(f"Freezing Layer: {layer_name}")
    
    print(f"{layer_name}\n")

#Save the modified file (can save as new doc with .saveas())
doc.save()