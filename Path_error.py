import json
list_paths = dict(
    Images = [r'D:\Desktop\Test\Images', ['bmp', 'png', 'jpeg']],
    Texts = [r'D:\Desktop\Test\Texts', ['txt', 'doc', 'docx']],
    Documents = [r'D:\Desktop\Test\Documents', ['xlsx', 'pub', 'accdb']],
    Presents = [r'D:\Desktop\Test\Presents', ['pptx']],
    Videos = ['D:\Desktop\Test\Videos', ['mp4']],
    Sounds = [r'D:\Desktop\Test\Sounds', ['mp3']],
    Programms = [r'D:\Desktop\Test\Programms', ['py']]
)
if input('Print "Y" to reset settings: ').lower() == 'y':
            with open('conf.txt', 'w') as fw:
                        json.dump(list_paths, fw)
            with open('conf2.txt', 'w') as fw:
                        json.dump(r'D:\Desktop\Test', fw)
