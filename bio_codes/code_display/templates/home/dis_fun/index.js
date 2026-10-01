const display = {
    gen : {
        info : 'Displaying genetic functions such as sequencing, comparison and distribiution',
        proj : ['DNA Sequence','Phylogenetic Tree', 'Punnet Squares', 'Sequence Alignment']
    },
    cell : {
        info : 'Cellular funcitons and effects of various stimuli on end products',
        proj : ['Cellular Division','Cellular Pathway']
    },
    gross :{
        info : 'Know your anatomical structures better',
        proj : ['Skeletal Database']
    }
};



const info_dis =document.querySelector('#info_dis')
gen.nodeValue();

function gen() {
        info_dis.textContent = 
        <>
            <h3>{display.gen.info}</h3>
            <p>{display.gen.proj}</p>
        </>
    };
    
function cell(){
    info_dis.textContent = 
        <>
            <h3>{display.cell.info}</h3>
            <p>{display.cell.proj}</p>
        </>
    } ;
    
function gross(){
        info_dis.textContent = 
        <>
            <h3>{display.gross.info}</h3>
            <p>{display.gross.proj}</p>
        </>
    };
    