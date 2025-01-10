 // for testing
    public function temporary(){
        $path =  FCPATH . 'public/uploads/testing/';
        $images = scandir($path);
        $removedfile[] = 'removed';
        $renamedfile[] = 'renamed';
        $number = 5000;
        $supportedextentions = array('jpg', 'jpeg', 'png');
        foreach ($images as $image){
            if ($image === '.' || $image === '..') {
                continue;
            }
            
           $filepath = $path.'/'.$image;
           $imageinfo = pathinfo($filepath);
           $extension = $imageinfo['extension'];
           if(!in_array(strtolower($extension), $supportedextentions)){
            rmdir($filepath);
            $removedfile[]= $filepath;
            continue;
           }
           if(file_exists($filepath)){
            $newname = $path.'/'.$number.'.'.$extension;
            rename($filepath, $newname);
            $renamedfile[$filepath] = $newname;
            $number++;
           }
           continue;
        }
        $data = array($removedfile,$renamedfile);
        pre($data);die; 
    } 