package Code;

/**
 * Comment intégrer la librairie ardoise.jar dans votre projet Eclipse
 *
 * 1/ Créer un dossier "libs" dans votre projet Eclipse
 * Clic droit sur votre projet -> New -> Folder
 *
 * 2/ Copier ardoise.jar dans le dossier "libs"
 *
 * 3/ Déclarer ardoise.jar comme librairie externe pour votre projet
 * Clic droit sur ardoise.jar (dossier "libs") -> Build Path -> Add to Build Path
 */

/**
 * Importation des classes :
 * - PointPlan
 * - Segment
 * - Ardoise
 * qui sont fournis dans la librairie ardoise.jar
 */
import java.util.ArrayList;
import ardoise.*;

/**
 * Classe TestArdoise
 * Validation de l'intégration de la librairie ardoise.jar au projet Eclipse
 */
public class TestArdoise {
    
	public static void main(String[] args) {
		ThreadA ardoise=new ThreadA();
		ardoise.start();

	}
	static class ThreadA extends Thread{
			@Override
			public void run() {
	        Ardoise ardoise = new Ardoise();

			/****************************tour****************************/
			Segment seg1= new Segment(new PointPlan(9,100),new PointPlan(20,100));
			Segment seg2= new Segment(new PointPlan(20,100),new PointPlan(20,198));
			Segment seg3= new Segment(new PointPlan(20,198),new PointPlan(9,198));
			Segment seg4= new Segment(new PointPlan(9,198),new PointPlan(9,100));
			Quadrilatere Rectangle=new Quadrilatere(seg1,seg2,seg3,seg4);
			Rectangle.setNomForme("Tour");
			/*****************************fin tour*****************************/
			
			/*****************************oiseau*****************************/
			Segment seg5 = new Segment(new PointPlan(118,13),new PointPlan(123,20));
			Segment seg6 =  new Segment(new PointPlan(123,20),new PointPlan(128,13));
			
			Chapeau Oiseau1=new Chapeau(seg5,seg6);
			Oiseau1.setNomForme("oiseau1");
			
			Segment seg7= new Segment(new PointPlan(133,30),new PointPlan(136,32));
			Segment seg8= new Segment(new PointPlan(136,32),new PointPlan(138,30));
	
			Chapeau Oiseau2=new Chapeau(seg7,seg8);
			Oiseau1.setNomForme("oiseau2");
			
			Segment seg9= new Segment(new PointPlan(142,14),new PointPlan(144,17));
			Segment seg10= new Segment(new PointPlan(144,17),new PointPlan(146,14));
			
			Chapeau Oiseau3=new Chapeau(seg9,seg10);
			Oiseau1.setNomForme("oiseau3");
			/*****************************fin oiseau*****************************/
			
			/*****************************montagne*****************************/
			Segment seg11 = new Segment(new PointPlan(3,14),new PointPlan(43,3));
			Segment seg12 = new Segment(new PointPlan(43,3),new PointPlan(112,14));
			Segment seg13 = new Segment(new PointPlan(112,14),new PointPlan(3,14));
			Triangle montagne1=new Triangle(seg11,seg12,seg13);
			
			montagne1.setNomForme("Montagne 1");
			
			Segment seg14= new Segment(new PointPlan(152,7),new PointPlan(166,3));
			Segment seg15= new Segment(new PointPlan(166,3),new PointPlan(172,7));
			Segment seg16= new Segment(new PointPlan(172,7),new PointPlan(152,7));
			
			Triangle montagne2=new Triangle(seg14,seg15,seg16);
			montagne2.setNomForme("Montagne 2");
			/*****************************fin montange*****************************/
			
			/*****************************étoile*****************************/
			Segment seg17= new Segment(new PointPlan(170,52),new PointPlan(173,45));
			Segment seg18= new Segment(new PointPlan(173,45),new PointPlan(177,52));
	
			Chapeau branche1=new Chapeau(seg17,seg18);
			
			Segment seg19= new Segment(new PointPlan(177,52),new PointPlan(184,57));
			Segment seg20= new Segment(new PointPlan(184,57),new PointPlan(177,60));
	
			Chapeau branche2=new Chapeau(seg19,seg20);
			
			Segment seg21= new Segment(new PointPlan(177,60),new PointPlan(174,66));
			Segment seg22= new Segment(new PointPlan(174,66),new PointPlan(170,60));
			
			Chapeau branche3=new Chapeau(seg21,seg22);
			
			Segment seg23= new Segment(new PointPlan(170,60),new PointPlan(164,57));
			Segment seg24= new Segment(new PointPlan(164,57),new PointPlan(170,52));
			
			Chapeau branche4=new Chapeau(seg23,seg24);
			/*****************************fin étoile*****************************/
			
			ArrayList<Forme> A=new ArrayList<Forme>();
			A.add(branche1);
			A.add(branche2);
			A.add(branche3);
			A.add(branche4);
			GF etoile=new GF(A);
			
			/*****************************La casa*****************************/
			Segment seg25= new Segment(new PointPlan(80,140),new PointPlan(180,140));
			Segment seg26= new Segment(new PointPlan(180,140),new PointPlan(180,198));
			Segment seg27= new Segment(new PointPlan(180,198),new PointPlan(80,198));
			Segment seg28= new Segment(new PointPlan(80,198),new PointPlan(80,140));
			
			Quadrilatere Corps_maison=new Quadrilatere(seg25,seg26,seg27,seg28);
			
			Segment seg29= new Segment(new PointPlan(120,170),new PointPlan(140,170));
			Segment seg30= new Segment(new PointPlan(140,170),new PointPlan(140,198));
			Segment seg31= new Segment(new PointPlan(140,198),new PointPlan(120,198));
			Segment seg32= new Segment(new PointPlan(120,198),new PointPlan(120,170));
			
			Quadrilatere porte_maison=new Quadrilatere(seg29,seg30,seg31,seg32);
			
			Segment seg33= new Segment(new PointPlan(80,140),new PointPlan(130,100));
			Segment seg34= new Segment(new PointPlan(130,100),new PointPlan(180,140));
	
			Chapeau Toit_maison=new Chapeau(seg33,seg34);
			/*****************************fin la casa*****************************/
			
			ArrayList<Forme> B=new ArrayList<Forme>();
			B.add(porte_maison);
			B.add(Toit_maison);
			B.add(Corps_maison);
			GF maison=new GF(B);
			
			ardoise.ajouterForme(Rectangle);
			ardoise.ajouterForme(Oiseau1);
			ardoise.ajouterForme(Oiseau2);
			ardoise.ajouterForme(Oiseau3);
			ardoise.ajouterForme(montagne1);
			ardoise.ajouterForme(montagne2);
			ardoise.ajouterForme(etoile);
			ardoise.ajouterForme(maison);
			ardoise.dessinerGraphique();

			try {
				ardoise.dessinerGraphique();
				sleep(3000);
				ardoise.deplacer(Oiseau1.typeForme(), 10, 20);
			}
			catch (InterruptedException e){
				e.printStackTrace();
			}
	    }
	}
}
