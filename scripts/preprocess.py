from nuscenes.nuscenes import NuScenes
import nuscenes.nuscenes as nu

def save_data(scene):
    image_name = scene['name']
    
    return

nusc = NuScenes(version='v1.0-mini', dataroot='./../nuscenes_mini', verbose=True)

for scene in nusc.scene:
    fst = scene['first_sample_token']
    sample = nusc.get('sample', fst)
    print(fst)
    
    while sample["next"] != '':
        for cam in ['CAM_FRONT', 'CAM_FRONT_LEFT', 'CAM_FRONT_RIGHT', 'CAM_BACK', 'CAM_BACK_LEFT', 'CAM_BACK_RIGHT']:
            camera_data = nusc.get('sample_data', sample['data'][cam])
            
            _, boxes, _ = nusc.get_sample_data(camera_data['token'], box_vis_level=nu.BoxVisibility.ANY)
            # for box in boxes:
                # print(f"Category: {box.name}, Box: {box}")
    
        sample = nusc.get('sample', sample['next'])