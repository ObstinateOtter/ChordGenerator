function updateWindow(){
    var note = document.getElementById("note").value;
    var mode = document.getElementById("mode").value;
    document.getElementById("current").innerHTML = "Chords for "+ note + " " + mode;
    updateTable(main(note,mode))
}

function main(n,m){

    function issublist(lst1,lst2){
        for(let val of lst2){
            if (!(lst1.includes(val))){
                return false
            }
        }
        return true
    }

    function LShift(lst, n){
        for(i=0;i<n;i++){
            lst.push(lst.shift())
        }
        return lst
    }

    function scale(root,mode){
        let arr = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
        let n = arr.indexOf(root)
        let lst = LShift(arr,n)
        if(mode == "Major"){
            var alg = [0,2,4,5,7,9,11]
        }else{
            var alg = [0,2,3,5,7,8,10]
        }

        let notes = []

        for(let i of alg){
            notes.push(lst[i])
        }


        return notes
    }

    function possibleChords(scl){
        
        function Maj_Min(L){
            return [L[0],L[2],L[4]]
        }
        function dim(L){
            return [L[0],L[3],L[6]]
        }
        function maj7_min7(L){
            return [L[0],L[2],L[4],L[6]]
        }
        function sus2(L){
            return [L[0],L[1],L[4]]
        }
        function sus4(L){
            return [L[0],L[3],L[4]]
        }

        let lst = ['A','A#','B','C','C#','D','D#','E','F','F#','G','G#']
        
        let chords = []
        for(let i of scl){
            let maj_lst = scale(i,"Major")
            let min_lst = scale(i,"minor")
            
            let note = {
                "std":{
                    [i]: Maj_Min(maj_lst),
                    [i + "m"]: Maj_Min(min_lst),
                    [i + "dim"]: dim(LShift(lst, lst.indexOf(i)))
                },
                "7th":{
                    [i + "maj7"]: maj7_min7(maj_lst),
                    [i + "min7"]: maj7_min7(min_lst),
                },
                [i + "sus2"]: sus2(maj_lst),
                [i + "sus4"]: sus4(maj_lst),
            }            

            chords.push(i);
            for(let variant in note){
                if(variant=="std"){
                    for(let type in note["std"]){
                        if(issublist(scl,note[variant][type])){
                            chords.push(type)
                        }
                    }
                }else if(variant=="7th"){
                    let flag = true
                    for(let type in note["7th"]){
                        if(issublist(scl,note[variant][type])){
                            chords.push(type)
                            flag = false
                        }
                    }
                    if(flag){chords.push("---")}
                }else if(issublist(scl,note[variant])){
                    chords.push(variant)
                    
                }else{
                    chords.push("---")
                }
            }
        }        
        return chords
    }
    
    let notes = scale(n,m)
    let lst = possibleChords(notes)

    return lst;
}

function updateTable(chords){
    let table = document.getElementById("chordTable");
    let rows = table.rows;
    let colCount = rows[0].cells.length;
    let i = 0;
    for (let col = 1; col < colCount; col++) {
        for (let row = 0; row < rows.length; row++) {
            rows[row].cells[col].innerText = chords[i]
            i+=1;
        }
    }
}