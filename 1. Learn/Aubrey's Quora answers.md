# Background
- The idea here is to gather [Aubrey's answers to Quora questions](https://www.quora.com/profile/Aubrey-de-Grey) so that they can be searched more easily.
- Note that the goal is to *only* have those of his answers that are relevant to SENS. Aubrey also talks about mathematics on Quora, and that generally won't be of interest to us.
- Newer questions at the top.
  - It isn't clear to me whether it's better to have them at the bottom or the top.
- It would be nice to have a Python script that would scrape these automatically and store them at some easily-accessible URL...
- The script would ideally get not only the answers, but also Aubrey's responses to comments.

# Questions

##### How can I apply to SENS for funding?
2017.10.08 - http://www.sens.org/research/grant-submission-process

##### What is the significance of the failure of monoclonal antibodies that remove amyloid beta as an attempt to slow the progression of Alzheimer's disease to longevity research?
2017.09.25 - Less than most commentators say. Abeta may or may not be causative in AD, and if it is there are many ways in which it could be, but the important thing to remember is that AD is complicated, which means that the repair of more than one of its features may deliver more than the sum of the benefits arising from repairing each one in isolation. We have Abeta removal in our back pocket now as a tool that can be combined with other tools (such as tau removal) as and when the latter are developed. Whether it’s needed remains to be seen, but I’m very happy that we now have the option.

##### Why are billionaires that support the SENS agenda not really funding it?
2017.09.25 - Yeah… well, the thing about not funding someone is you don’t tend to be all that forthcoming about why you decided no… but my best inference is that there is no one answer, every HNWI is different. Sometimes they don’t think non-profits work. Sometimes they are scared that the approach is still unproven so they want to wait and see. Sometimes their spouse is virulently opposed. Sometimes they think other causes are more important. Sometimes they have a bad vibe about me personally. Sometimes they don’t like to do things that other HNWIs are not doing and they don’t consider Thiel to be a reliable first-mover. For each of the above reasons I could (but I won’t!) name at least one HNWI who I believe is substantially an example.

##### How much money does Aubrey de Grey need to find a cure?
2017.09.22 - Short answer: $1 billion over 10 years would do it with high probability.

Longer answer: clearly the question is not whether but when aging will be brought under comprehensive medical control. Thus, the right question is how much money is needed, over what time period, to hasten that time to the point where money will not make much difference any more because the rate of progress is limited by the simple difficulty of the research. See above for the number!

Key other number: at current funding levels we are going so slowly that (by my current estimate) we could easily end up delaying the defeat of aging by a decade. Therefore, even low-balling the expectations, every $2 spent in supporting this work would save a life. That compares very favourably with anything else.

##### What's been the progress, if any, on the WILT (Whole-body interdiction of the lengthening of telomeres) strategy?
2017.07.23 - It’s been slow but steady. On the telomere control side, other groups have made nice progress in inhibiting telomerase-mediated elongation (see especially Jerry Shay’s 2015 paper on 6-thio-2′-deoxyguanosine) and we have developed a much faster and cheaper assay for ALT that will facilitate the discovery of anti-ALT drugs. On the stem cell replacement side, we funded a study to look for the ability of early-generation telomerase-knockout haematopoietic stem cells to rescue longevity in late-generation telomerase knockout mice, and it worked (it was tricky because we needed to rescue their gut problems with another mutation) but we could only afford to do a small study so we barely made it to statistical significance and we haven’t published it. Our parallel work on the gut, led by Graca Almeida-Porada at Wake Forest, made modest progress but unfortunately we have had to suspend that project because of lack of funds.

I remain hopeful that we can get WILT to work - but I also remain hopeful that we won’t need to, because simpler therapies will work well enough. In particular, the progress in cancer immunotherapy over recent years has been dramatic, and it might just be enough to make WILT unnecessary. We won’t stop working on WILT until we’re sure that that is the case, though!

##### Do induced pluripotent stem cells reverse the intracellular junk that accumulates with aging?
2017.05.25 - Sure they do, but not because they are pluripotent: simply because the divide. Cell division shares out any junk between the daughter cells, so it dilutes it away.

##### Aubrey de Grey, what do you mean by "longevity escape velocity"?
2017.05.26 - The thing you’re overlooking is that the “first-generation” panel of rejuvenation therapies will not be perfect: it will mostly plug the gaps that evolution has left in our in-built damage-repair machinery, but it won’t do so 100%. (Let’s just define the damage that it does repair as the easy damage and the rest as the difficult damage.) There is nothing to stop us from applying those therapies every year, never mind every 30 years - but because of their incompleteness, however often we apply them we will still get back to biologically the same age (i.e., we’ll be carrying the same quantity of damage) at some point (I generally guess chronological age 90, but that’s a total guess) as we were just before we first applied the therapies. And the problem is, that the overwhelming majority of the damage that is present at that point will be difficult damage.

Thus, the only way we will be able to re-rejuvenate these people is if we have improved the therapies. And of course this carries on being true until such time as the therapies become truly 100% comprehensive, which quite probably will never happen. Hence the need to keep pushing ever closer towards that probably-unachievable goal. LEV is simple the minimum pace at which we need to do that, in order to keep one step ahead of the problem.

The good news is that LEV slows down as time passes, because the smaller the remaining gaps in the therapies, the longer it takes for that still-too-difficult damage to become abundant enough to make us sick.

##### Could CRISPR-modified CAR-T-cells clear senescent cells?
2017.03.27 - I’m guessing the question is stimulated by this recent study:

http://www.nature.com/nature/journal/v543/n7643/full/nature21405.html

Short answer: maybe, but it won’t be the end of the world if not, because there are now quite a few promising-looking ways to clear them. Our latest focus in this area is somewhat related: we’re starting to look at improving clearance with another arm of the immune system, NK cells, which are already known to clear most senescent cells following would healing so may be easiest to augment to do that job more thoroughly.

##### What does Aubrey de Grey think about the potential reversal of ageing in humans through Dr. Keizer's modified FOXO4-p53 interfering peptide?
2017.03.25 - The result is important, and the “DRI” technology used to do it is potentially even more important because it is so broadly applicable. We’ve known for a while that the elimination of senescent cells is a major plank of rejuvenation, and this is a further confirmation, with the advantage that it is underpinned by good scientific understanding of the mechanism.

##### What drugs can enhance the autophagy function of cells?
2017.03.14 - It’s important to remember that “autophagy” refers, strictly, to the processes that transport waste products to the lysosome, and not to the destruction of that waste once it gets there. This is not semantic hair-splitting, because it’s seductive but counterproductive to assume that enhancing autophagy will sustainably reduce the abundance of undigested waste in the rest of the cell. If there is too much such waste and the root cause of that is the lysosome’s inability to destroy it, no amount of enhancement of autophagy will help. And unfortunately, impairment (such as in aging) of lysosomal catabolic function seems to result, mainly, from the fact that that function is never 100% comprehensive even in youth, hence some types of waste accumulate there throughout life, with eventual upstream “traffic jam” consequences.

So there are plenty of answers to the question as asked, but really it’s the wrong question. The better question is, what drugs can sustainably enhance the lysosomal elimination of waste? And the answer to that, at present, is “none”. Enhancing that elimination requires enhancing the lysosome itself, which can only be done by giving it additional enzymes so that it can destroy stuff that it normally can’t. We’ve made good progress on that in a couple of key areas, atherosclerosis (oxidised cholesterol) and macular degeneration (derivatives of vitamin A), and both those programs have now been spun out into startups (Human Regenerative Biotechnologies and Ichor Therapeutics). We’ve recently started a new program in this area, targeting neurofibrillary tangles in Alzheimer’s.

##### Will Aubrey de Grey do a talk in France (or has he done one)?
I’ve given quite a few talks in France over the years. I haven’t honestly noticed a particularly greater susceptibility to this sort of thinking than elsewhere.

##### Which advice would Aubrey de Grey give to somebody with lupus erythematosus or arthritis as an autoimmune disease?
I’d advise consulting a medical professional, rather than anyone like myself whose doctorate is a PhD. We’re working on rejuvenating the immune system, which will certainly address autoimmunity to some extent as well as regular immune dysfunction, but our work on this, as on everything, is early-stage research and is years from being ready for prime time.

##### What does Aubrey de Grey think about the longevity pill Niagen?
Aubrey:
> Tim has it right.

Tim Amann:
> I obviously can’t speak for Aubrey de Grey, but I suspect he wouldn’t be interested in, or advocate for, Niagen. Niagen is a calorie restriction (CR) mimetic - a substance that supposedly mimics the effects of CR, which has been shown to have a significant longevity effect on short-lived organisms, but far less so on longer-lived organisms. Summing up the many things he has said about CR in the past, I would say he thinks CR would have little effect on human longevity. I wouldn’t say that he is against it. It’s just not his focus and not a game-changer in relation to aging.
> 
> In short, de Grey’s strategies are centered around removing and repairing the seven major forms of damage caused by aging (analogous to maintaining a classic car). He’s not attempting to stop or reverse the aging process (meaning he’s not trying to stop the damage from aging from occurring), which he would say is not doable for a very very long time due to the complexity of human metabolism.
> 
> CR mimetics are based on the idea of slowing the aging process (Niagen, Resveratrol, Metformin - pretty much any current “anti-aging pill”), but again, these will likely have little effect on longer-lived species like humans. Metformin will be going through a clinical trial, so we’ll know more soon, but I wouldn’t expect anything dramatic in relation to lifespan. I think de Grey estimated CR can provide, at the most, 2 to 3 more years in humans.
> 
> Niagen could potentially provide some benefits from a healthspan perspective (increased energy, potentially), but evidence is lacking. Time will tell.

##### Is it true that thanks to our technologies on aging, we have exceeded the limit of “in a lived year, we have gained more than a year to live”?
Definitely not. The rate at which the headline life expectancy numbers rise, which is a couple of months per year, does understate the situation for any given individual (basically because the headline numbers are statistical constructs generated from people born in different years), but it definitely doesn’t understate it enough to mean that we are already at “longevity escape velocity”. However, I remain of the view that we have at least a 50% chance of getting to that point within the next 20 years.

##### Is the first 5 year old mouse already alive (and is ongoing an anti-aging trial)?
Probably not - the current record of just one week shy of five years probably can’t be beaten by any practicable genetic manipulation. But what matters much more is what can be achieved using only interventions performed when the mouse is already alive, and ideally already middle-aged. At present the record for that is less than four years, so reaching five years is a very tall order - but I think there’s a good chance that the first such mouse will be born within five years.

##### Are there any good ways to invest in anti-aging research/therapies?
Wow… I’m not sure where to start with this one. The number of ways to invest in this space is exploding, and the most basic Google search will lead you to a host of opportunities. If you want more sophisticated advice on the best investment options. write to me at aubrey@sens.org and I’ll be happy to help.

##### How do T-lymphocytes have a lifespan that is infinite (according to my teacher)? Don't the telomeres get shorter until the cell dies?
T cells (and also B cells) turn on telomerase when they are in the highly proliferative phase, so they compensate for the telomere shortening that you’re thinking of. However, this telomerase activation weakens in old age, and that’s generally thought to be a big contributor to the age-related decline in the power of the immune system.

##### What's Aubrey de Grey's position on telomerase activators?
I’m very much on the fence. The question of whether telomerase activation will have decisive long-term negative consequences in terms of cancer is one that we cannot currently answer with confidence. Therefore, I very much endorse and support the research and clinical trials currently underway on telomerase activation, while at the same time SENS Research Foundation itself is heavily engaged in research to do the opposite, suppressing telomere elongation as an anti-cancer strategy.

##### Can we increase our maximum lifespan just by clearing senescent cells, beta amyloids, transthyretin and by immune system rejuvenation? Can we reach 150 years old?
What George said. The body accumulates many types of damage in the course of its normal operation, any of which will kill us on schedule unless it is eliminated (i.e., repaired) before it reaches fatal levels,however well we fix all the others. Fixing one major type of damage will **somewhat** slow down the accumultion of others, and I’ll admit that the magnitude of this interdependence may be a fair bit more than I would have thought before the results of the past few years in the senescent cell elimination area, but still, adding 70 years to today’s average lifespan of 80 is highly unlikely until we can rather thoroughly repair all seven of the main categories of damage.

##### What is your review of SENS Foundation?
Check out our annual report which should be released around the end of January.

##### What are the best indications of progress in anti-aging technologies we can expect by the end of 2021?
Clinical trials of most (though probably not all) of the key damage-repair interventions that SENS Research Foundation pursues. See here:

[Project|21 Announcement](http://www.sens.org/outreach/press-releases/project21-announcement)

###### Comments
- Randall Burns: You had said in a previous posts you thought longevity studies on effects of adult HGH supplementation on mice who either lack growth hormone or lack the known growth hormone receptor might be a good idea. Do you think we may see studies in that area any time soon?
  - Aubrey: It’s a rather obvious experiment and not very difficult except insofar as any lifespan experiment is expensive, so I’m surprised that it still hasn’t been done. If I had the money I’d commission it!
  - Randall Burns: Do you know anyone who could give the approiximate budget needed?
  - Aubrey: Probably $20k minimum…

##### What is Aubrey De Grey's response to the skepticism of some scientists such as PZ Myers?
The personal answer is that generally I don’t waste my time on people who are more interested in attracting readership by writing derogatory and pathetically uninformed drivel than in contacting me for actual facts.

The more important answer is that careless professional skeptics do a lot of harm by seducing the public into believing their uninformed skepticism and thereby sapping funding for life-saving research. I wrote about this in my most recent editorial for Rejuvenation Research, in reaction to a piece in Scientific American by Michael Shermer that uncannily resembles the Myers one.

##### Does the fact that different negligibly senescent species have different lifespans prove that aging is not caused by damage but by a genetic program?
By definition, any difference in lifespan between two negligibly-senescent species is caused by differences in extrinsic causes of death, not by aging.

The difference in rate of aging between species that DO age is certainly determined by genetics, but not in the way that you seem to be thinking. It is determined by the degree of comprehensiveness of the arsenal of genetically-encoded machinery that repairs damage as that damage is generated. There is not, by contrast, any program that actively creates such damage (or inhibits that anti-aging machinery) on purpose. See the paper I wrote on this topic last year.

##### If people with Laron Syndrome do not exhibit any lifespan extension, can we extrapolate the same to calorie restriction in humans?
Calorie restriction works less well in longer-lived species, because long famines are rarer than short ones so the selective pressure to maintain the genetic machinery to adapt to them is less. See my paper in Gerontology from 2005. The same applies to any genetic or pharmacological emulation of CR, since by definition they work through the same pathways as CR itself does.

##### What does Aubrey de Grey think of the possible appointment of Jim O'Neill as the head of the FDA?
I think he would be a huge asset. He combines two vital qualities: the vision to see what needs to be done in such an influential role, and the diplomacy to carve through the thicket of vested interests that so often impedes necessary change. I hope he gets the job.

##### What does Aubrey de Grey (or other leading longevity researchers) think about cord blood banking?
My view is that it is a useful thing to do, but not for anti-aging purposes, because the progress we make in (ten, let alone) 50 years in medical research massively exceeds the difference in difficulty between doing things with young cells versus old cells. I have made the same argument in relation to germ line gene therapy.

##### Of all the startups funded by Breakout Labs, which are Aubrey de Grey's favorites?
Hard to say, actually, because they’ve funded quite a few really amazing companies - some of them on my introduction. Among the very first crop, I must mention Arigos, Immusoft and 3scan, all of which are focused on sensational technologies.

##### How does Alagebrium work in breaking crosslinks up?
The most recent work on this is the following study from the lab of David Spiegel, whom we fund to work on glycation-induced crosslinks:

[The unique reactivity of N-phenacyl-derived thiazolium salts toward α-dicarbonyl compounds.](https://www.ncbi.nlm.nih.gov/pubmed/23186164)

##### What does SENS foundation think of a gene network stability model of ageing and the medical research strategies resulting from it?
It's a nice study (and I know Fedichev quite well). But the problem with all studies of this kind is that it isn't informative to demonstrate that one's model reproduces the pattern of aging and lifespan that is seen in nature, because it turns out that lots of models do that, including extremely different models. And one can't really say that there's a case for a treatment that is inspired by a particular model but not by another that reproduces real-world aging equally well.

##### If cancer cells are immortal, how do they solve the problem of error accumulation of DNAs and proteins?
Proteins are no problem because any garbage is diluted out every time a cell divides. DNA errors are a big problem for most cells of a cancer, but for the cancer overall they are vital, as they are the source of the genetic diversity that lets the cancer outwit the immune system etc.

##### How many different forms of intra- and extracellular 'gunk' will need to be cleaned up for the SENS anti-aging approach to work?
Great question. We don't really know, of course. At present our focus is on just three of each (intra and extra), but transthyretin's role in the extreme elderly has only been known for a few years, and I would be quite surprised if new examples don't turn up pretty soon. The good news, though, is of course that the same methodology should lead to the therapies for each case, such that we can take advantage of what we learned for the first examples to speed up the pipeline for later ones. So actually, and especially when we factor in the longevity escape velocity dimension, the viability and timetable of the SENS strategy doesn't depend too badly on how many such compounds will need to be cleaned up.

##### What's Aubrey de Grey worth, and where did he get the money to personally support SENS research?
As of now my net worth is around $2M, of which only a small minority is in any way disposable. I inherited about $16.5M from my mother in 2001, of which I donated about $13M to SENS Research Foundation (or more precisely to our UK affiliate). Of the remainder, on which inheritance tax was payable so it was reduced to about $2M, I spent the majority on the house where I now live, in the Santa Cruz mountains.

So far so good - but I will take this opportunity to mention that I and my colleagues at SENS decided in 2011 to spend this money over a period of five years, which we judged to be a good balance between getting it put to good research use and keeping us afloat long enough to bring in additional money. The research has gone great, but the fundraising is still mighty dicey. All help gratefully received!

##### Do aging of stemcells determine the longevity of an organism alone since short lives of normal body cells do not affect the organism's longevity?
No, for several reasons. The main reasons are:

- there is aging of material outside the cell, such as crosslinking of the extracellular matrix that causes loss of elasticity, leading to things like hypertension
- many cells just hang out for life, neither dividing nor being replaced, and they age internally
- cells can get damaged and refuse to die when they should, or to stay quiescent when they should

##### Why is Aubrey de Grey so optimistic about his predictions, considering no SENS therapy has been shown to extend lifespan yet?
The lack of such data is irrelevant to the assessment of whether SENS is likely to work on the kind of timeframes I’ve predicted. The idea that it would be relevant is akin to the idea that cars can’t work because no individual component of a car exhibits motion when burning gasoline is poured on it. Medicine is a branch of engineering, and engineering doesn’t work additively. Putting it in more biological terms: each type of damage in the body is protected against by a different set of genes (though the sets overlap), so evolution will gravitate to a quality of those genes that results in the respective types of damage all becoming life-threatening at about the same age. Thus, fixing any one such type of damage (or even most of them) will not appreciably postpone the ill-health of old age.

##### What does Aubrey de Grey think about the way Michael Fossel and Bill Andrews are trying to tackle aging?
Short answer: yes but not yet, and the much-discussed diversity of expert opinion on this topic actually entirely misses the point.

Long answer: it’d definitely be very valuable if we had a way to really really totally control cancer that did not involve preventing telomere elongation, which we may indeed have within not too long if the recent progress in cancer immunotherapy continues, but we may not. If we don’t achieve such control, it may well be that the only way we can develop to control cancer really thoroughly is by very robustly preventing telomere elongation, which will inevitably result in the creation of problems in rapidly-renewing tissues (such as the gut and the blood) even if those problems don’t currently exist (which is the focus of expert debate that I mentioned above). We’re working on doing exactly that in combination with stem cell therapies to alleviate any such side-effects. But for now, I’d say one should be cautious, because we can’t yet even tell reliably whether someone has early-stage cancer, let alone cure it.

##### Would someone who is 80 benefit from SENS therapies or is it too old to rejuvenate them?
Depends on their state of health. Best way to think about this is in terms of how many more years the person can be expected to live, rather than how long ago they were born. The bad news is that the things we can control as regards how much longer we can live are much less influential than the things we can’t control, such as our genetics.

##### At the exponential rate at which longevity movements are advancing, can radical life extension be achieved gradually over the next decade?
No, I don’t think it will be gradual. I believe that life expectancy will actually level off for the next decade or two before damage repair therapies arrive, and that when they do it will skyrocket. There will be a rather sharp cusp.

##### Which, if any, of the existing alleged anti-aging supplements does someone like Aubrey de Grey believe in and use personally?
I don’t personally take anything, but that should not be interpreted as advice to others not to. My way of looking at this is to start from three very basic principles:

1. Nothing simple, which means nothing we have today, can possibly benefit most people dramatically, only very slightly. That’s because both the body and its aging are really complicated, and one can’t dramatically alter the behaviour of a really complex system by simple means, other than if the system already has inbuilt machinery to respond to that simple stimulus. There is one example of such machinery, namely the response to famine, but for obvious evolutionary reasons (basically just that long famines are rarer than short ones) the response to famine in long-lived species like humans is much milder than in short-lived ones.
2. Everyone’s metabolism is different, so the only way to really tell what works for you is to listen to your body, not to trust books.
3. I’ve been tested very thoroughly several times over the past 15 years and I always come out with a very young biological age. Thus, for me the best policy is to be conservative in terms of doing anything new: if it ain’t broke don’t fix it.

##### When will aging be reclassified as a disease?
Aging (defined as the physiological decline that everyone currently experiences with advancing years after about 40) unquestionably causes astronomical amounts of suffering, in the modern world adding up to more than all other human experiences put together. Thus, it is exceptionally demoralizing to see educated people continuing to find such crass ways to put it out of their minds, like comparing it with left-handedness. Aging is unequivocally a medical condition that is potentially amenable to medical intervention, and as such it is vital that such interventions be developed as soon as possible and therefore that the quest to do so be supported, not trivialized.

Whether aging should be called a disease, however, is a question with additional ramifications. “Disease” - like “immortality” and “cure” - is a word that has an established meaning that has already been obfuscated to the detriment of progress: in particular, it has been extremely unfortunate that conditions such as Alzheimer’s are called diseases, because that gives the impression that they can be “cured” - eliminated from the body entirely, like an infection - when in fact they are parts of aging and as such are side-effects of being alive. I am OK with calling aging an “uber-disease” that encompasses all aspects of the ill-health of old age, but no more. But the thing that really matters is not whether we call aging a disease but whether we call it a condition for which treatments can be approved and reimbursed. That, I’m overjoyed to say, is a question on which there has recently been fantastic progress, spearheaded by Nir Barzilai and colleagues, in the form of the TAME trial for metformin. The definition of the endpoint, in terms of the presence of more than one of the key features of age-related ill-health, is a perfectly good practical definition of aging, and even if the TAME trial itself is unsuccessful, the precedent that it has laid down in terms of how to structure future clinical trials will stand and will be copied increasingly often. That makes me very happy.

##### Can we try all present day rejuvenation technologies combined on mice?
Sure. The problem is that any such experiment needs to be done on a rather large scale, so as to identify which components are working, are interacting synergistically, or are interacting antagonistically. But this is a key part of implementing SENS properly, so it must be done soon. We are unable to embark on it thus far at SENS Research Foundation due to lack of funds, but we’re trying our best to change that!

##### According to the paper doi: 10.1038/nature20578 does it mean that we completely stopped the aging processes in mice?
No, nothing of the kind. This is a suspension of embryonic development at a very early stage, and it has nothing to do with aging of an adult animal.

##### Can triphala\chebulic acid break glucosepane crosslinks? Can it increase lifespan?
I asked my colleague Michael Rae to look into this, and here is his answer:

There's certainly no good evidence that it does either. While chebulic acid is being promoted as an inhibitor and even breaker of advanced glycation endproducts (AGE), there are numerous deep limits and/or flaws in the research underlying this claim.

First, all of the research reporting inhibition or breakage of AGE by chebulic acid was conducted in Petri dishes, reacting pure isolated chebulic acid with artificially-generated so-called AGE molecules (I'll come back to that last point in a moment). It is always best to be skeptical of such "in vitro" studies, because the way that molecules behave in a living organism can often be quite different from the way it behaves in an isolated system. This is especially so for the two halves of the question here — AGE and glycation products on the one hand, and compounds like chebulic acid on the other. Chebulic acid is a phenolic acid, part of the family of compounds generally referred to as "polyphenols," and such compounds tend to be very heavily metabolized by enzymes in the gut microbiome, the intestine, and finally the liver before being absorbed (if they are absorbed at all) into the circulation.

I can find no studies that monitored the absorption and biotransformation of chebulic acid into metabolites, and indeed, the authors of several scientific papers on chebulic acid have highlighted lack of such studies as an important limitation to the physiological significance of their reported results using the compound. One study attempted to get a preliminary handle on this issue using a much less expensive simulation of digestion using a series of reactors with different conditions mimicking the conditions of different parts of the GI tract on chebulic acid and related molecules in Terminalia chebulia. The results of this study suggests that much of an oral dose of either compound will be degraded into simpler molecules in the upper GI tract, and that much of what reaches lower down will largely be metabolized by the gut bacteria into compounds called urolithins, which are degradation products of polyphenols that (on the one hand) tend to be better absorbed than the original compound, but which (on the other hand) tend to be metabolized into still other compounds that are less reactive than the original urothelin, and whose biological activity is unknown. So it seems unlikely that any intact, pure chebulic acid will even reach your tissues to exert the effects reported in the Petri dish studies, let alone at a concentration adequate to exert any meaningful biological effect.

Additionally, the formation and maturation of glycation products is dictated by the specifics of the complex physical and chemical environment of the body, including factors like temperature, the concentration of sugars, the structure of proteins, and the presence of transition metals and free radicals in body fluids. While the studies on chebulic acid in glycation chemistry have been carried out at body temperature, they have not attempted to simulate physiological conditions in other ways, making the results suspect.

Then there is the matter of what these in vitro studies are actually testing. The compounds that have been labeled AGE in recent studies are not clearly AGE at all, are even less likely to be AGE encountered in the body, and are fairly clearly not glucosepane. Some studies have used proteins from the lens of the eye and reacted them with threose, a degradation product of vitamin C that has been hypothesized to be involved in the crosslinking of such proteins because vitamin C itself is present in the human lens at about double the concentration of glucose. However, studies that have looked for the early products of threose reacting in proteins in the body on the way to forming AGE have failed to find any, either in the human lens or elsewhere, and there's no particular reason to think that such products would lead to the formation of glucosepane even if they did form.

Another study, which purported to show not only the inhibition of the formation of early glycation products but the actual breakage of mature AGE, generated the glycation products by reacting glycated circulating proteins with collagen, but did not actually test to see what product they had made;

[FEEDBACK FROM "GLYCOSENS PANEL" FITS IN HERE]

Overall, it seems unlikely that chebulic acid breaks /any/ AGE crosslink in the body, and even less likely that it can break glucosepane.

<Nathan Wailes TODO: Get the links below working.>

[21308613 24759763 20659546[uid] - PubMed - NCBI]

[In Vitro Bioaccessibility, Human Gut Microbiota Metabolites and Hepatoprotective Potential of Chebulic Ellagitannins: A Case of Padma Hepaten® Formulation](http://www.mdpi.com/2072-6643/7/10/5406/htm)

http://www.jbiopharm.com/

[World Journal of Otorhinolaryngology...](http://www.wjgnet.com/2218-6247/)

Statistical optimization of process parameters influencing the biotransformation of plant tannin into gallic acid under solid-liquid fermentation Panda BP, Mazumder R, Banerjee R - J Pharm Bioall Sci

Hyperglycemia, Diabetes and Vascular Disease

[ETD Home...](https://etd.ohiolink.edu/rws_etd)

##### Which is a better area for investing personal effort: curing causes of aging or improving artificial intelligence?
It's a great question, and a complex one. Importantly I know quite a few AI researchers who cite as their main motivation (or a big one) for working in that field the possibility that it could help solve aging. Ben sent me an elaboration of his question that he was unable to include in the question, so I'll quote it here:

---

For a person who is interested in potentially making a large difference, which is a better investment of personal effort, between these two choices-

1. Curing aging-related damage (like the work being done by SRF Home | SENS Research Foundation, run by Aubrey de Grey)
2. Improving artificial intelligence (e.g. to achieve strong AI faster)

I researched this question online and didn't find any discussion on this question (but maybe my Google-fu was weak).

And this is a question about investing *personal effort*, not charitable donations. It seems like the safest choice when it comes to *charitable donations* is to donate to both kinds of causes. I.e. "Diversification is the only free lunch on Wall Street". It's really hard to predict the future, after all, so diversifying donations might be the best way to maximize the odds of helping to create a big difference.

But when it it comes to personal effort on the scientific side, it seems like specialization is key- trying to make a personal contribution in both areas is probably suboptimal. It's very hard to be excellent at two extremely challenging fields.

Some people might naturally gravitate one way or the other, and this way humanity is exploring both options, which is great, since we can't know ahead of time, which is most important. But many young people could go either way, and a choice should be made, and I'm curious what people think is the most promising choice for someone on the fence.

To me, it seems like a person whose top priority is to cure aging, might actually prefer to focus on AI, since maybe strong AI would be the fastest route to figuring out solutions to aging. This seems like a possible two-for-one, if relevant strong AI is more achievable in the near term.

Part of my thinking on this has come from seeing how strong AI compares to humans in games like Chess, Othello, etc.

Aubrey de Grey and I are both familiar with Othello, and Othello is orders of magnitude simpler than the human body. But *even though* Othello is relatively "easy", AI can radically outperform maximum human intelligence when playing Othello (the same goes for Chess, and maybe soon Go as well, given the recent exciting news).

So, I have great hopes for what AI will eventually be capable of.

OR!

It's also possible that focusing on curing aging could be extremely important in speeding up the development of strong AI. This could be due to potential improvements in human intelligence due to understanding biological mechanisms better, or like, if Marvin Minsky had gotten many more years of peak cognition, maybe he (or someone like him) would have already been able to generate a huge AI breakthrough sooner than humanity would otherwise generate it.

Or, perhaps most important, it could convince billions of people to care a LOT more about the development of AI, and how we approach AI when it comes to safety issues, power issues, sharing the wealth, etc., and this would both speed things up and improve the likely outcome.

Does Aubrey de Grey, or anyone else who is a possible expert on how each area might influence the other, have any thoughts on this question? I guess it's a question of "possible timelines, depending on how we invest in each area, and how each timeline influences the other".

Bonus question: which area is easiest to make a contribution in. Is it easier to make a contribution when it comes to biology, or when it comes to artificial intelligence, if a person is starting close to zero?

---

So to answer: well, having worked extensively in research in both areas, I will try to add to the points Ben already raised. First, from the philosophical perspective, I think he is coming from a standard utilitarian position and asking the question as an "effective altruist" as it's often called these days. The impact of progress in each field on subsequent progress in the other one is part of the question, but there are many other dimensions: for example (a) would progress in strong AI be a good thing or would it destroy the human race, (b) can we actually make remotely accurate enough predictions of the amount of impact our time would have to make a rational decision at all, or should we stick to things that have smaller but more immediate and thus predictable humanitarian benefit (this is the position of some leaders in the EA movement), etc. I honestly don't think there is any way to give a strongly defensible answer.

##### Why would telomeres of different chromosomes in the same cell erode at different rates?
There are two known (to me!) reasons why telomeres would shorten at different rates per cell division in a particular cell lineage, and they both simply say that longer telomeres shorten faster. One is that telomere shortening is partly due to DNA damage, and longer telomeres present a bigger damage target. The other is that telomerase acts preferentially on shorter telomeres because there are telomere binding proteins that inhibit it. But obviously, anything that just says longer telomeres shorten faster does not say anything about a population of cells, because it is a negative feedback loop. Perhaps I could say more i you would elaborate on what motivated your question.

##### Aubrey De Grey, in the long run, would nanobots be required to extend healthy life indefinitely?
The only realistic answer (apart from "What counts as a nanobot?") is "Maybe, maybe not". I think it's likely that non-biological solutions to all medical problems, including aging, will play a progressively increasing role in medicine, and that this will be driven substantially by miniaturisation. But whether such technology will ever be absolutely required, we cannot say.

##### Can we use calories restriction on dogs even if we don't know the amount of calories of their food?
Yes, Purina sponsored such a study many years ago. Search PubMed using "lawler df kealy rd " - the 13th hit is the initial report, and the first 12 are all followup analyses.

##### What does Aubrey de Grey think of Alcor Life Extension?
My position on Alcor is very public, so I’m surprised to see this asked. I’m signed up, and I’m also a member of their scientific advisory board (both since 2003 I think). They are, as they have long been, the leading organisation in a movement that does hugely important life-saving work.

##### Could Longevity Escape Velocity happen by 2050 if we donate more to SENS?
I’m looking at more like 2035 to 2040 with 50% probability subject to funding, but it’s by no means certain to be achieved even by 2100, so whatever year from 2035 to 2100 you pick, absolutely a donation will increase the probability. The more specific question is, how much would each dollar help? I do the calculation this way:

- about 40 million people die of aging each year worldwide
- our current budget is around $4 million
- I estimate that we could go about 3x faster if it were $44 million
- that factor will diminish as progress is made and others pile in, but it still probably means a ten-year delay (i.e., with current funding my 50% date is 2045–2050)
- therefore, $40M per year for maybe 10 years could save 400M lives - a dollar per life
- And that’s not even taking into account that this sort of saving of lives is rather more extreme than other sorts, when measured in terms of life years added

##### Is recent research on the cleansing of scenecent cells in mice as relevant as it seems?
Yes it is. This is the best demonstration yet of the value of one of the SENS strands. It is becoming increasingly impossible to maintain the previously almost universal assumption that repairing the damage of aging is far more difficult than slowing down its creation.

##### Of the 7 types of aging damage, which has the highest probability of killing you first?
None - there's no order. They are all held back by different sets of genes, so the selective pressure that maintains those genes over generations depends on all types of damage being bad for physiological performance at about the same age.

##### What is the bottleneck for anti-aging research: money or human capital?
David Gobel is absolutely right: the main thing is that the people with the greatest ability to help are also overwhelmingly people whom a lot of other people respect, and who are keen not to dissipate that respect by publicly supporting a cause that so many people still view as quixotic. But the reason why that matters so much is that the answer to your question as stated is undoubtedly money. The crusade already has absolute world leaders of all relevant disciplines firmly on board to perform the R&D that is needed to get truly comprehensive anti-aging medicine working, but they are paralysed by lack of funds to get on with that job.

Saying that, though, it's still not obvious that the right thing for you to do would be to get wealthy, because generally that takes time. You might make more of a difference sooner by getting to know people who are already wealthy and visionary, and getting them to see past their reputational risk aversion.

##### Why doesn't Larry Page of Alphabet Inc. give Aubrey de Grey's SENS Research Foundation all the money it needs to do what must be done?
An even better question would be "Why didn't he donate a decade ago when Peter Thiel did?" In September 2005 there was a small dinner party hosted by Peter at the Four Seasons in San Francisco, which was the first time the either I or Cynthia Kenyon had met either Peter or Larry. Since then, Peter has funded SENS to the tune of around $6M (though for sure we wish he'd give more!), and Cynthia to a much lesser degree. Larry has gone the other way (insofar as Cynthia is now at Calico). Neither Peter nor Larry has been short of relevant scientific information. So I guess the message is that there is no way to understand the decision-making process of wealthy people.

##### Should the NIH allocate more of its funds to aging research?
Yes or no, depending on what is meant by the term “aging research”. The majority of the $30B NIH budget already goes on research into conditions that mainly affect the elderly, but unfortunately nearly all of that is spent on the quixotic attempt to “cure” specific age-related diseases, in the sense that one cures an infection (eliminating it from the body), which is obviously impossible for conditions that are age-related, since a condition can only be age-related in the first place by virtue of being a side-effect of being alive. At the other end of the spectrum, a small but still respectable amount (around 150M/y) goes on biogerontology research, but again the large majority is devoted to the wrong type of work, namely to increasing our understanding of phenomena that have next to no biomedical potential (most conspicuously, the life-extending effect of calorie restriction or its genetic or pharmacological emulation). Both these errors are fueled by the insistence of virtually everyone (and biologists on both sides of the divide are the most guilty, since they are the ones who should most know better) on the patently false dictum that there is some kind of clear distinction between age-related diseases on the one hand and “aging itself” on the other, when in fact any such distinction is purely semantic. The only chink of light in this sad state of affairs is that a few visionaries within the NIH, led by the head of the NIA’s division of aging biology Felipe Sierra, are working internally to break down this barrier via a vehicle named the Geroscience Interest Group. However, despite the verbal support of Francis Collins (head of NIH), it seems very much as though this initiative will never progress beyond tokenism in terms of redirection of actual dollars, because of the horde of short-termist vested interests arrayed against it and in favour of the status quo.

##### Is aging research more financially constrained or more talent-constrained?
Financially, by a huge margin. Every area that needs effort has the intense interest of at least a few of the world leaders in the relevant fields; they just need the resources to get on with the job.

##### How does parabiosis affect aggregation of damaged proteins/lipofuscin?
I’m not aware of any direct investigation of this issue - but in the absence of that I think we can still say with reasonable confidence that the impact in at least some cell types, such as neurons and cardiomyocytes, would be minimal. It seems that such cells are highly disinclined to do anything, under any stimulus yet explored, that would eliminate such material: they neither divide, nor exocytose it, nor magically activate any hitherto silent enzyme that degrades it. I would be very surprised if any change to the extracellular environment of such cells, which is what parabiosis brings about, would be any different.

##### Is there a unifying factor in aging?
Inevitably it depends what you mean by “factor”. If you mean the question in the narrowest terms, which would be equivalent to “is there a single pressure-point that w emight be able to tweak so as to postpone aging a lot?”, we can be very sure at this point that the answer is no. If you mean “is there an inherent tendency foe the variousconstituent processes that contribute to aging to gravitate to a roughly common rate, as defined by the age at which they start to impair health?”, then the answer is definitely yes (though with the qualification that I highlighted a decade ago when I coined the term “protagonistic pleiotropy”). But maybe you mean something in between.

##### Do naked mole rats have more powerful kidneys than rats? Can kidney parameters explain the lifespan difference between different animals?
Yes and no, in the most useless sense. The two most key things you must always keep in mind about aging and longevity are (1) that in order to live a long time, the organism has to do everything right, and (2) that everything interacts with everything else. Jointly, these things mean that no single component of the organism - whether defined at large scale, such as a particular organ, or at a microscopic scale, such as a component of cells - can play a dominant role in determining the variation in lifespan across species - even cross closely-related species, like naked mole rats versus mice. But they also mean that no component that actually does anything can play a zero (or even negligible) role. The only things that can play a negligible role are things that don’t do anything - which is, of course, what SENS focuses on, namely the various types of life-long accumulating damage that the body does to itself in the course of its normal operation. The reason why that makes sense is that damage only temporarily doesn’t do anything; eventually there is enough of it to get in the way.

##### How far are we from being able to extend the lifespan of a mice to 10 years?
Quite a long way - probably, I’d say, further away than we are from reaching longevity escape velocity in humans. The problem is that mice are shorter-lived than humans for a reason, or more precisely for a whole host of reasons: in a nutshell, their in-built anti-aging machinery has bigger gaps in it than ours does. That means it’s harder to plug all those gaps well enough to make a several-fold (which is what you’re describing) difference to lifespan. I think we have a good chance to get mice to five years within under a decade, and that’s even with interventions started in middle age; but getting to ten years is a far bigger leap from that than it may sound. Conversely, getting humans to 150 is 90% of the work to get them to 1000, because plugging most of these gaps (i.e., enough to get anything much at all) is a lot harder than in mice, not least because we’d be a lot unhappier if 10% of the humans were inadvertantly killed than if 10% of the mice were. Counterintuitive, I know, but pretty obvious when you think through the above.

##### What would be needed to change in our organism in order for us to be immortals?
Nothing. All that is needed in order to eliminate the rise with chronological age in our risk of death in the coming year (which is what I am going to presume you mean by being immortal, though I strongly disapprove of that word being used in that way) is to develop medicine to repair the self-inflicted damage of aging faster than it is being created. That’s what SENS Research Foundation is doing. Some of our work may lead to therapies that are “one-off”, i.e. they really are changes to the organism (typically the addition of genes), but even those probably won’t really be one-off, because gene therapy won’t hit every cell.

##### What are the most important human aging related AGEs after glucosepane?
That is a hugely important question - especially since the better way of phrasing it is “how sure can we really be that there are not in fact other ECM modifications that are even more important than glucosepane in contributing to aging?”. The short answer is: nowhere near as sure as the literature implies. The long answer falls into four parts.

1) Are there non-crosslinks that matter? There are of course lots of AGE non-crosslinks, such as carboxymethyllysine. My belief has always been that such adducts are basically harmless at the levels that accumulate in a currently normal lifetime - an example of protagonistic pleiotropy arising from their pathway of formation (and thus the genes that suppress their formation) having so much in common with those for crosslinks - but I might be wrong.

2) Are there non-AGE crosslinks that matter? There probably aren’t any that are formed non-enzymatically: the best-known example is dityrosine, which for sure is less abundant than glucosepane, but we must keep looking. But there are reports that a well-known enzymatically-generated one, EGGL, increases with age, and it is unclear whether this is a result of a shifting dynamic equilibrium between creation and destruction or whether there is just no destruction. In the latter case, EGGL would need to be addressed, even though it’s not an AGE.

3) Are there known AGE crosslinks that are of comparable or greater abundance than glucosepane? Definitely not in human collagen, but we must not forget that there are other ECM proteins that have been studied less well. The only real candidate right now is K2P, a lysine/lysine link that is very abundant in the lens; this is probably a weird special case caused less by the fact that the protein (crystallin) is not collagen and more by the very high ascorbate concentrations.

4) By far the scariest option: are there bona fide AGE crosslinks that accumulate more rapidly with age than glucosepane but have escaped detection? We have been funding an outstanding group in the UK, that of Jonathan Clark at the Babraham Institute, to work in partnership with our Yale group (that of David Spiegel), and their focus has been exactly this question. So much of science is limited by only seeing what you are looking for, and the more we examine the methods that have been used to analyse aged ECM the less confident we become that nothing has been missed. After all, glucosepane itself was missed for a very long time. And the very bad news right now is that we are desperately short of funds, so Jonathan’s work is currently on hold. We badly need to resume it. Our recent donation from Michael Greve (see SRF Home for details) will match any other donation for this project (and for most of our other projects), but we still need to actually obtain those other donations.

##### Is aging a body's attempt to prevent cancer?
For some bad definitions of aging the answer would be “mostly yes”, but for good definitions of aging the question doesn’t make sense, because nearly all cancers are parts of aging. Most cancers predominantly affect people who are chronologically elderly, because they arise from the lifelong accumulation of damage to a cell’s DNA, arising as side-effects of normal metabolism, that enables it to resist the body’s many anti-cancer mechanisms. And anything that results from the lifelong accumulation of damage rising from metabolism should be viewed as part of aging, whether or not we give it a disease-type name.

##### Can we live until 200 if we clear AGEs, amyloid, senescent dells, and if we inhibit atherogenesis? Would it be enough?
No it would not. For a start, none of those measures would postpone cancer even by a decade. See SRF Home for a more thorough answer.

##### Can IT progress like more speed and deep learning accelerate the anti-aging progress? For example, move the LEV from 2050 to 2035?
You mean the Methuselarity, i.e. the point at which we reach LEV. I already put that at having a 50% chance of achievement by the late 2030s. But to answer the substance of your question, my answer is a little complex and revolves around the messy and incremental manner in which I am pretty sure the initial transition to a post-aging world will be implemented. Basically what will happen is that a wide range of damage-repair therapies will be implemented, they will each kinda work, and they will each substantially postpone the ill-health of a subset of people (the people who are accumulating that type of damage a little faster than other types) and slightly postpone the ill-health of a lot more people, the ones who are getting other types of damage up to a pathogenic level at about the same time, by virtue of the plethora of knock-on effects that exist (the interaction between systems within the body). The damage repair itself is probably not going to be much accelerated by clever algorithms and big data, in my view, because we basically already know what to do and the rate-limiter (unless you count funding for the research, which is very definitely the rate-limiter today) is the scientific process, the grinding through discoveries of technical details that we don’t know. But the situation is different for the knock-on effects: they vary quite a lot in magnitude from person to person, as a result of innumerable details of metabolic variability, so in that area I think that big data and deep learning and so on have a substantial chance to identify personalised optimisations that amplify the effects and thereby postpone ill-health by a greater amount. And yes, that means hastening the Methuselarity. Probably only by a few years, but those will be very welcome years.

##### Do you know of any viable and robust criticism of SENS research project?
I’m intrigued by both the answers given by others so far - for different reasons, unsurprisingly. Duane’s reply makes little sense to me because we focus very strongly on rejuvenating the immune system: indeed, in my original formulation immune senescence was its own category before I realised that it was better described as subsumed within cell loss and cell death-resistance. Nathan’s answer is actually not so much intriguing as enlightening, to others if not to me, since it expresses very honestly the difficulty that so many basic scientists have in appreciating the difference between science and technology. For a technologist, the fact that we don’t yet know (despite decades of work) whether protecting mtDNA will slow aging (or, more precisely, will be a necessary component of a panel of therapies that jointly slows aging) is of little importance: if it might slow aging, and it seems to be hard to determine whether it will, and we have a fair idea how to do it, let’s just go ahead and develop a way to do it, and if our achievement ends up being unnecessary in the end, no harm done. Whereas, if we spend another few decades trying to figure out whether mtDNA damage matters and not developing ways to fix it, plenty of harm may be done, because we may fix everything else and thereby find out the hard way that yes mtDNA damage matters because people keep getting sick and dying on schedule. But this way of thinking is completely alien to basic scientists who find things out for the sake of finding things out. Conversely, technologists like myself are intensely frustrated by the fixation of basic scientists on phenomena that have long ago been shown to have minimal potential for humans (calorie restriction being the main one) resulting from the terribly interesting things that such interventions do to lab animals.

To answer the actual question: no. SENS has evolved in terms of its fine details, as new technologies such as iPS and CRISPR have come along, but the overall structure is still abundantly standing the test of time.

##### What does Aubrey de Grey think of minimal cells like JCVI-syn3.0 Minimal Cell?
They are a formidable technical achievement, but there is no knowing at this point how useful they will be in the development of future medicines etc. The first things to come from them may be improved understanding of metabolism, arising from identification of the function of the many essential genes whose function is currently completely unknown.

##### What does Aubrey de Grey think about MitoQ?
I think mitochondrially-targeted antioxidants are very worthy of more study. If anything can make antioxidants really work toslow down the creation of aging damage, it's these. But, I still think the jury is out as to whether they actually can. I was quite disappointed at Skulachev's failure to extend maximum mouse lifespan with his version of the same idea - I rather expected the result to resemble what happened with mitochondrially-targeted catalase (Schriner et al from a decade ago).

##### How is SENS research on longetivity different from Calico (owned by Google)?
Calico are being quite tight-lipped about their activities (as most private companies that don't need to raise money tend to be!), so to some extent one can only guess. But from their pattern of hiring, it's a good bet that they are focusing on trying to understand aging better, as a step towards figuring out how to postpone it. That's not surprising when you have a chief science officer (David Botstein) who is on public record that he doesn't have a translational bone in his body, but it's unfortunate, because the field has moved on from that attitude and it is now entirely orthodox to think in terms of intervention based on what is already known about aging, i.e. without finding out any more fundamental truths. We have of course tried to educate them on this, but thus far they have basically blown us off.

##### How can an expert in molecular simulation (molecular dynamics, Monte Carlo, etc.) help defeating aging and implementing SENS?
There are a few options, but they depend on your specifics. Best thing is if you email me at aubrey@sens.org and I'll get one of my colleagues to reply thoroughly.

##### What is Marc Tatar known most for doing within the biology/aging community?
He's a very strong cyclist - probably surpassed only by Siegfried Hekimi, who rode in one or two Tours de France in his day. He even ships his bike to conferences in the Alps and such like.

##### How does one break up Carbamylated Proteins?
We're looking closely at this new discovery, but let's be clear that at this point there is no evidence that this type of modification leads to crosslinking. It remains to be seen whether it matters at all.

##### What does Aubrey de Grey think of Ray Kurzweil's prediction about Longevity?
In a nutshell, we’re not all that far apart. We differ somewhat as regards what can already be done today (what he calls “bridge 1”), but regarding future advances we are on very much the same page.

##### Using cutting edge science and almost infinite funds, can we keep a human head alive for longer than normal human lifespan?
Absolutely not with today’s technology. Also, realistically it is very unlikely that the “autonomous” aspects of brain aging are unimportant enough that a brain’s aging could ever by substantially slowed down just by connecting it to a young-like blood supply. We’ll fix aging in general, brain included, before then.

##### What does Aubrey de Grey think of Maximum Human Lifespan, which seems to be about 115 years?
If you’re referring to the recent paper in Nature from Vijg’s lab, I have some issues with the statistical methods used but I agree with the conclusion. However, please understand that the conclusion says NOTHING AT ALL about what may be achievable with future medicine. It is all about how ineffective present (and past) medicine has been in alleviating aging.

##### What does Aubrey de Grey mean by “Aging is a phenomenon of physics, not biology”?
I mean simply that the underlying reason why complex living organisms age is the same as why man-made machines with moving parts age, namely that the laws of physics dictate that wear and tear happens and that it takes work to reverse the accumulation of that wear and tear.

##### If Aubrey de Grey was going to college this year, what would he have studied to become a researcher on aging? Does he think MD is an alternative?
I would recommend a general biology degree course. Aging affects the body at every level of organisation, so in order to understand it well one needs a good grounding in genetics, biochemistry, cell biology, molecular biology, physiology, the lot. An MD is not such good training because it mainly emphasises what we can already do today.

##### What organizations exist with similar missions as SENS?
If one defines our mission as the medical control of aging, there are (gratifyingly) a large and increasing number, both for-profit and non-profit. If one defines it more narrowly as the application of the SENS concept of damage repair/obviation to the molecular and cellular constituents of aging, so far there are none that take it on as a general mission, but there are now a few that are focused on specific examples of it. These include spinouts from SENS Research Foundation, such as Ichor , and also independent companies such as Unity. The rejuvenation biotechnology industry, which it has always been SENS Research Foundation’s goal to engender, is finally emerging.

##### Can Quercetin or drugs that use apoptosis induction increase health span in humans by killing senescent cells (that spread cytokines)?
We can’t know the answer to that until it is tried, but the preliminary evidence from rodent studies is promising. The other, necessary, big question is whether such drugs can be sufficiently selective so that they don’t also kill cells that we want to keep. If that turns out to be very hard, the alternative is to be more sophisticated and use genetic rather than pharmacological targeting. This is the approach that I have always advocated within SENS, and it is now being pursued by a new startup named Oisin that we work closely with.

##### Has Aubrey de Grey's knowledge of computer science made significant and concrete contributions to his research on aging?
A huge contribution, especially early on after I switched fields. Actually, to be more precise, it was not so much the knowledge as the way of thinking that is typical of CS, which is totally unlike what is typical in curiosity-driven fields. CS, being a mainly goal-directed field (a technological one rather than basic science), uses evidence very differently. And in the mid-1990s, the problem of aging was ripe to undergo the transition from discovery into translation (a transition that is still in progress, don’t get me wrong). I was in the right place at the right time for my skill set.

##### Is aging due to accumulation of malfunctioning cells or due to cell depletion?
I don't have much to add to Kurt's answer, which you don't seem to like. I don't understand why you are convinced that the problem of aging has to be too much apoptosis or too little. As Kurt says, sometimes it is one, sometimes the other, and sometimes neither. It just depends which cell type and which organ or tissue you are looking at. In SENS, too much apoptosis (more precisely, too little cell replacement) and too little apoptosis are two of the seven categories that I partition the many types of damage into, for the purposes of describing ways to repair or obviate that damage and thus maintain youth.

##### Why do telomeres matter in post mitotic c elegans?
Well, what exactly do you mean by "matter"? C. elegans are not completely postmitotic - they obviously have dividing cells in the germ line.

##### Does SENS Research Foundation have plans to start collaborating with, or to collaborate more closely with Calico, Human Longevity Inc., and/or Alcor Life Extension Foundation?
Calico: we hope so, but they have basically blown us off so far. They are being quite secretive about their plans, but from the range of people they are hiring they have not yet really got the message that damage repair is the way to go.

HLI: maybe, but the connection is less obvious there, because HLI are not (yet!) really in the business of defeating aging entirely; instead they are seeking to improve personalised medicine by sophisticated use of genomic sequence data.

Alcor: yes and no. I've been on their SAB for a decade but we don't work directly with them. However, their ex-CEO Tanya Jones, who was for five years our COO, is now CEO of a hugely exciting startup named Arigos (along with Steve Van Sickle, who preceded her as Alcor CEO) - they are working on a new method of cryopreservation that has huge near-term potential in the organ preservation market as well as being a potential game-changer in cryonics per se. We invested in Arigos when they set up.

##### If you want to hasten the anti-aging research, why should you donate to SENS Foundation instead of others organizations?
Thanks for the question, and to Tony for his very thorough reply. I don't have much to add, actually. SENS is a bona fide plan for defeating aging entirely, by repairing the accumulating damage that eventually kills us. Almost all other approaches entail, in one way or another, slowing aging down by taking advantage of the genetic machinery that underlies the response to famine. That concept used to seem really promising, as a result of the impressive life extension demonstrated both by famine itself and by its genetic or pharmacological emulation in laboratory organisms, but for a long time it has been obvious to anyone who was really being objective that such an approach would probably work far less well in longer-lived species (I wrote a detailed paper to this effect in 2005), and we now have conclusive data to prove it in the form of the two huge monkey calorie restriction studies that concluded in the past few years. It's therefore downright scandalous that people who should know far better are still pursuing that approach. Another approach is to optimise the effect of medicines that apready exist, using improved knowledge about individuals' genones and other omes - that's what Craig Venter's HLI is doing, basically - and again it's only going to have modest benefits at best.The other big reason to fund SENS Research Foundation is that some other organisations are indeed focused on damage repair, but only on the lowest-hanging fruit that will either make money or get publications really quickly. We respond to that by doing the opposite - prioritising the equally vital but hardest and thus most neglected areas. It definitely pays off - for example, six weeks ago we had our first publication in Science, arising from the work on crosslinking that we fund at Yale - but it takes a long time to do so, so it needs donors with just as much vision and patience as we ourselves have. And there sure aren't enough of those. My current estimate is that we are being slowed down by as much as a factor of three at present by shortage of funds, and that's in grave danger of getting worse soon, when the funds I donated in 2011 from my inheritance run out. So all in all, I believe we've made a strong case for being the right beneficiary for any donors who want themselves, their loved ones and humanity in general to stay truly heathy however long they live.

##### Could CRISPR be used to promt macrophages to 'clean up' atherosclerotic plaques?
Probably not on its own, because we think it is necessary to introduce new genes (from other species, probably bacteria), which CRISPR isn't designed for. But there is the alternative of doing a bone marrow transplant with genetically modified stem cells, which will enhance a subset of the subsequent macrophage population.

##### Is it within the realm of possibility that someone could be born with a genetic mutation that led to longer life...?
No, but the reason why not is subtle enough that you could certainly get away with it in fiction. There are mutations that confer 30% or so life extension in mice, but the overwhelming preponderance of both evidence and theory is that such mutations confer much less life extension in longer-lived species. (This inconvenient fact is assiduously swept under the carpet by a depressingly high proportion of the researchers who work on those mutations, but hey, their hands are tied as they have each other's grant applications to approve...)

##### How promising for Alzheimer's are the amyloid beta disrupting drugs from Eli Lilly and Biogen as of September 2015?
I'm very hopeful, but only because of what's coming. The clear message from the trials is that amyloid matters when it's the predominant issue but not when it isn't (well duh). To elaborate - the Biogen trial succeeded because it specifically recruited patients whose Abeta load was unusually high for their level of cognitive impairment. Tangles matter too, and maybe the earlier trials failed because too many of the patients were mainly suffering from tangles. Short story, this is aging in microcosm - a condition arising from the combination of multiple typesof accumulating damage. 

So, why an I hopeful? Because tau immunotherapy is coming! Tau moves between neurons, and there is pretty good evidence now that it can be grabbed by antibodies en route. It's early days... but I think this could be the area in which the value of combination therapies finally hits a home run. 

I expect that patients with fairly advanced (though not terminal) AD will benefit quite a lot from the removal of both tau and Abeta, in contrast to what we see with only removing one of them which is that only mild patients get any meaningful benefit. But but but, this all depends on the companies being sensible and not pandering to the drive for simplicity. I don't think removing tau on its own will do all that much better than removing only Abeta.

##### If we believe that we can slow or halt aging the future, would it be possible to reverse aging for people who were older at the time that such technologies were discovered?
Absolutely yes! - the whole of SENS is about damage repair, which is not exactly the reversal of the processes that created the damage, but is identical in terms of the outcome - one would be restored to the physical and mental performance of a young adult. Concerning DNA, there are various answers. One part of SENS entails putting backup copies of the mitochondrial DNA into the nucleus, so that mitochondria will always work whether or not their DNA is damaged. Damaged DNA can also be replaced just by replacing the cells that contain it, and I believe that until we have extended longevity many-fold we will probably get away with restricting ourselves to curing cancer, because other mutations don't accumulate fast enough. And if we want to look really far ahead, we don't have to worry about not having stored cord blood or whatever, because we can "average" the damaged DNA - no single mutation will be present in a majority of cells (or anything close), so we can just swap out sequences that we find only occasionally in favour of the majority sequence, without needing to know what the mutation did. (Of course this is rather easier said than done, but I did say "really far ahead"!).

##### Is [this article](http://www.bloomberg.com/news/features/2015-02-12/does-a-real-anti-aging-pill-already-exist-)a fair portrait of state-of-the-art anti-aging pharmaceuticals? Why, why not?
Well no, clearly not, since it's only about rapamycin. But as far as it goes it'sa fine article, yes.

##### Aubrey de Grey I've been studying aging for almost a decade now, and I'm a biochemist. I think the best approach to overcome aging is to have a whole-body replacement strategy, rather than repairing body. What do you think about this strategy?
There's not so much difference between replacement and repair as you're suggesting. In many ways the difference is purely semantic, revolving around the scale at which you're describing the procedure: in a car, for exampme, replacing the engine constitutes repairing the car, and replacing the spark plug constitutes repairing the engine, etc. Sometimes the scale that is practical will change over time - initially it may be easier to replace the whole heart with one built in the lab, for example, whereas later it will be easier to repair it by replacing individual cells and clearing our waste products and so on.

##### Does Aubrey de Grey have any opinion about the ketogenic diet?
Not really - diets are not my area of expertise, because what we can say for sure is that no diet seems to confer anywhere near the impact on aging that SENS seeks to achieve.

##### What does Aubrey de Grey think of the creation of Google Alphabet?
I'm not sure that there is all that much to think. It seems to me no more nor less than it is being stated to be - a reorganisation of their top-level organogram to reassure shareholders. As such, it seems like a good thing in that it insulates the more visionary entities like Calico.

##### What will the effects of life extension technology be on overpopulation? What models exist to predict population dynamics?
See this recent paper reporting the initial results of a project we funded to explore exactly that question (and related economic and political ones):

[Opportunities and challenges of a world with negligible senescence](http://www.sciencedirect.com/science/article/pii/S0040162515001985)

##### Why is Aubrey de Grey not raising funding for SENS through Crowdfunding?
We have used crowdfunding a little, and we're planning to ramp it up, but we don't see it as having the potential to make a big difference to our budget any time soon. The basic problem is that all our projects need six-digit sums annually, and that they don't have clearly defined timelines or deliverables. Of course they can be carved up into small subprojects that do, and whose costs are smaller, but then the problem becomes one of being inspiring: the subprojects are necessarily rather technical and hard to make attractive to the masses.

##### Do rates of biological ageing less than zero exist in humans? What does it mean?
They could indeed have been recovering from health issues, or else it could be a result of the unavoidable noise in the experiment - variations in parameters due to time of day, amount of sleep the person got the previous night, whether they were under psychological stress, a million things. More generally, my take on this study is that it is a very tantalising but extremely preliminary foray into the challenging area of longitudinal study of aging in early adulthood. A great start, but only a tiny part of the puzzle.

##### Is the creation of the Alphabet Holding good news or bad news for the long term plans of (Google) Calico?
No. I'm 99% sure it is purely a measure to soothe Google shareholders and will make no meaningful difference to the activities or fortunes of any of the components, including Calico.

##### What can I do to live as long as possible?
Your best bet is to give SENS Research Foundation lots of money, so as to hasten the development of medicines that will bring aging under genuine medical control, and thus to increase the chances that that will happen in time for you. Failing that, persuade other people to do so.

This is not a flippant answer. While all the things that others here have recommended have some value, for most people the effect on lifespan will be tiny. The only way to live even a decade longer than you otherwise might is to benefit from future medicines.

###### Comments
- Hannes Hoffmann: While the things others have recommanded probably do not make people die a lot later, i think they make them die healthier. So in case your chance to benefit from future medicine depends on your state of health in 20 or 30 years, leading a healthy live now might be important for livespan.
- Aubrey: Actually even that is only marginally the case. It's true that people who live the longest also tend to have the shortest period of disease before they die, but the bulk of that correlation is due to the short-lived and least healthy end of the spectrum. In other words, there is a big difference in both healthspan and lifespan between living averagely and living unusually unhealthily, but a very small difference between living averagely and living unusually healthily.

##### What has improved or changed since 2007's Ending Age book was released? Are there new advances in any of the researches that the book mentions? Has the approach for any of the 7 lines of action changed, evolved or advanced?
There have been many big advances, yes, both in our own work and in independent work - see our annual reports, our newsletter (subscribe!) and our news updates at [SENS Research Foundation](http://sens.org/) for details. Arguably even more heartening is that no, there have been no major updates in our approach as a result of new discoveries - it is robustly standing the test of time. There have essentially only been good surprises, i.e. advances that have given rise to short cuts, making one or another SENS strategy easier than we thought it would be.

##### What does Aubrey de Grey think of 2045 Initiative?
Neither, actually: I just think SENS is closer to being achieved. I could be wrong, though, so I strongly support Dmitry's efforts - if uploading gets to work before SENS does, I'll be in the line for it. Dmitry feels the same: what matters is to save lives, not how it's done.

##### Assume that projects led by either Dmitry Itskov or Aubrey De Grey succeed in significantly extending human lifespan. How likely is it that politics and legal issues will cripple the rise of immortality on trivial grounds for several years?
There is no chance at all that any of these arguments for restricting access will prevail. The universal desire to remain healthy will dominate; it will be impossible to remain in power if one opposes, or even is neutral about, the delivery of that technology to one's people.

##### Has the life span of a particular blue whale been monitored? How much was it?
Bowhead whales are generally thought to live even longer than blue whales.

##### Can transcriptomics be used in lieu of lifespan studies to determine if an intervention slows or speeds aging?
Depends what you mean by "aging". It's easy to come up with reasonable definitions of aging that make the answer to your question obviously yes or obviously no.

##### Is the TA-65 yet proven to be effective in lengthening telomeres in humans?
My information is that yes, there is clear telomere elongation. Whether that is a net positive for postponing age-related ill-health remains an open question.

##### If there is a major breakthrough in aging research that can increase life expectancy by at least 5-10 years, how long will it take to verify it?
The first thing to remember is that the life extension effect will be merely a side-effect of postponing ill-health. This means that the time it takes to verify it and convince people also centres on health; people won't need to be convinced of the life extension effects, because they already just don't like getting sick. Second, the time taken will depend on how the therapy works - specifically, on whether it repairs the damage of aging or only slows down the further creation of that damage. The latter takes a lot longer to verify;  the good news is that repair will almost certainly be easier.

##### What do Matt Kaeberlein and Aubrey de Grey think of each other?
We don't actually know each other all that well. He's an excellent scientist. I don't really know what he thinks of my science, but I strongly suspect he is not so dismissive of it as the 2006 critique of SENS that his friend Pete Estep somehow persuaded him and half a dozen other researchers to sign.

##### Does Aubrey de Gray make a valid point about reversing aging in the coming decades?
Sanjay - what parts of my publications on this topic do not sound strongly fact-based to you, exactly?

##### Why are so many mainstream researchers in aging skeptical of Aubrey de Grey?
The main reason for the residual resistance to SENS among mainstream researchers is fear of association with the idea that radical life extension is foreseeable. The problem is outlined in my most recent editorial in Rejuvenation Research:

[Longevity Sticker Shock: The One Remaining Obstacle to Widespread Credentialed Support for Rejuvenation Biotechnology](http://online.liebertpub.com/doi/abs/10.1089/rej.2015.1732)

##### What does Aubrey de Grey consider to be the strongest argument against ending aging?
As Johnty predicted, my answer is that there is no remotely strong argument against ending aging.

###### Comments
- Issa Rice: This isn't an answer. "Strongest" doesn't mean "strong"; it means "strongest out of all the arguments, even if they are all weak".
- Aubrey: Indeed - but "not remotely strong" means that all arguments are so ridiculously weak as to be unrankable.

##### Do you expect cancer immunotherapy to significantly increase the human lifespan?
Not on its own, no, simply because the complete edarication of all cancer would not - it would only add a couple of years. This is a simple mathematical consequence of the fact that a lot of life-threatening conditions rise exponentially in incidence with age, all of them by roughly 10% per year; since "only" 20-30% of people die of cancer, that means it only takes a couple of years for the total incidence of all the others excluding cancer to overtake the total including cancer.

##### Why is the average human life expectancy increasing?
The main thing that I don't think has been said yet is why life expectancy in the developed world has continued to increase even though the impact of hygiene, vaccines etc has long reached diminishing returns. Basically, the reason is "cohort effects" - improvements to health early in life that keep people healthier at a given chronological age than people born earlier. The main cohort effect is probably early-life (including prenatal) nutrition. In other words (for illustration), because on average people born in the West in the early 20th century were in more prosperous and thus better-fed families than people born in the West in the late 19th century, they were "born younger" and stayed biologically younger than the older cohort throughout their lives, with the result that they lived longer.

##### How much will joining the Methuselah Foundation's "300" actually accelerate longevity research?
Here's how I measure it. I estimate that there is a 50% chance that we will achieve a decisively comprehensive level of medical control over aging (what I've called "longevity escape velocity") within 20-25 years, so long as we are not slowed down by lack of funds. I also estimate that at present the lack of funds is slowing our rate of progress by a factor of about three. That factor will fall over time, since the main thing causing lack of funding is lack of progress - each small step forward pushes a few more people over the edge into thinking it's a worthwhile venture - so at a rough guess I think that we will lose about five years in the long run if funding stays low for the next ten years. (I estimate that after 2025 the amount of progress we've made even with low funding will have been enough that there is unlikely to be all that much trouble getting the necessary funds.) The level of funding I think we would need in order to eliminate those five years is about $100M per year, as against the current level of $5M per year; however, because we (obviously) prioritise the most impactful projects, the first additional $1M would make at least twice as much difference as the last one. Each year, roughly 40 million people die of aging worldwide. So, combining all those estimates, one gets a number of roughly $2 donated today per life saved, which compares very favourably with other ways of spending money (and of course the definition of "life saved" is rather stronger than it is for other medical interventions, since it entails adding a lot more to the recipient's healthy and total life expectancy).

Note that the above is written in terms of donations to SENS Research Foundation, the charity of which I am now the Chief Science Officer, as opposed to our sister charity the Methuselah Foundation, which I co-founded and which (as the question notes) is the one that has the "300" club. We have identical missions, but by and large SRF is the one that does and funds research, whereas MF is the one that runs prizes.

For anyone who is wondering why organisations involved in the "effective altruism" movement are not advocating more strongly that donors should support SENS: the main reason is that there is a lot of skepticism within such organisations concerning the ability of researchers to estimate the difficulty of their research. GiveWell, for example, talk a lot about the value of such research and about their intention to get more active in that area, but in the end they still only recommend charities that help the developing world. There is a lot of debate within that community concerning whether this is a valid policy. For example, see this piece by Peter Singer:

[Should We Live to 1,000?](http://www.project-syndicate.org/commentary/the-ethics-of-anti-aging-by-peter-singer)

##### If all SENS objectives are realized would humans be eternally in their 20s?
Basically yes, both mentally and physically (except that of course SENS would not erase one's memories of adult life!). Better, well, there might be some such side-benefits, yes, but they would mainly arise from secondary uses of the technologies.

##### How long will it take for anti-aging technology to reach escape velocity under current SENS funding?
That depends on how long one expects the funding to stay at current levels. At present I think we could be going roughly three times faster than we are if we had $50M per year to spend rather than only $5M. But as we make more progress, it will inevitably become easier to raise more funds. Taking all such things into account, I currently estimate that if we jumped to he $50M/year level tomorrow we would have a 50% chance of reaching LEV within 20-25 years, and every three years that go by with funding staying stagnant adds two years to that number.

##### What, in your opinion, is the most likely technology/medicine to dramatically change the way we age?
See http://sens.org/ for my answer, obviously...

##### Do mice with mega-telomeres live longer?
No. Telomeres play a very different role in the trade-off between different potential causes of age-related death in small mammals versus large ones. Check the work of Woody Wright and (independently) Vera Gorbunova on this.

##### Aging: How is the The Longevity Fund different from the SENS Foundation?
Well, the Longevity Fund is a venture fund focused on supporting companies working to postpone age-related ill-health, whereas SENS Research Foundation is a biomedical research charity focused on funding in-house and university-based research projects to postpone age-related ill-health. So we're in the same field, and the same part of the world, but our methods are complementary. Laura Deming and I are good friends though :-)

##### What can someone do to live forever? I've read about parabiosis. Would younger family members donate their compatible blood to be used in elected infusions? Would a clinic agree to that, or would health care professionals decry it as unethical?
Evidence is accumulating, not least from the parabiosis work you mention, that significant rejuvenation may be possible via restoration of youthful levels of certain factors in the blood. However, as noted in another answer here, there will certainly be aspects of aging that are not affected by such procedures, and since ultimately you are as old as your weakest link this means that more is needed in order to postpone ill-health substantially. And unfortunately, a lot of that "more" is still in the early stages of development (not least by SENS Research Foundation).

Thus, depending on exactly what you mean by "advanced age", I don't have the sort of answer you're probably looking for. There is nothing available today that can get someone to what I've termed "longevity escape velocity", and there almost certainly won't be for at least another 20 years. I do very much advocate signing up to be cryopreserved, because that really is a lifeline - and an increasingly strong one, as research progresses in solving the key challenges inherent in minimising the damage done to tissues by the cryopreservation process. But mainly what I advocate is not focusing too strongly on oneself. As a 52-year-old who is dedicating his life to this cause, I can tell you that what gets me out of bed in the morning is not the thought that my work is incrementing my own chances of making the LEV cut by a percent or three. It is that my work is saving a ridiculous number of lives - getting others to make the cut, whether or not that cohort includes me. I don't know whose lives I'm saving, because I don't know how soon these therapies will arrive, but I do know how many lives - over 100,000 for every DAY that I hasten the defeat of aging. The same applies to money as to time, of course: based on my current estimates of how much the lack of funding is slowing down critical-path research, I calculated recently that it only costs $3 to save a life by contributing to this work.

##### What is a reasonable estimate as to the degree of longevity extension that could be realized via stem cell therapy alone?
I would be very surprised if we got more than five years that way - in fact I would guess no more than two years. The way to calculate this is to list the major killers that would not (as far as we know) be significantly delayed by stem cell therapy - which, unfortunately, include both atherosclerosis and cancer. That kind of logic is why SENS Research Foundation has elected to go the route of diversity, addressing everything that underlies every cause of death whose incidence rises exponentially with age.

###### Comments
- Lucas Karl Hahn: I remember reading in your book something about replacing cells with stem cells every 10 years or so to stop both aging and cancer, I think it may have been called WILT. Is this different from stem cell therapy?
- Aubrey: Close but no cigar. First, there's no such thing as "aging and cancer" by my definition, becaue cancer is part of aging. Second, WILT is not to stop both [non-cancer aspects of] aging and cancer, it's only to stop cancer. Third, WILT entails not only stem cell therapy but also gene therapy to remove cells' ability to extend their telomeres even if they mutate a lot. Read Chapter 12 again!

##### Is Elon Musk right when he says that the agreement of geneticists to not reprogram DNA could hamper anti-aging efforts?
Well, first let me note that this is the first time I've seen any remark from Musk concerning the defeat of aging. I've met him, but only once, years ago. From what is written in the interview, I infer that he has a good understanding of the basic nature of the problem (specifically that it is a chaotic one that will only yield to a divide-and-conquer solution) but that he has not spent much time learning about current efforts to solve it. His remark about reprogramming DNA suggest that he has not yet seen past the idea of germ-line genetic engineering to turn us into a species that is still in essential ways human but yet doesn't have aging any more - which is grossly oversimplistic, but I don't mean that harshly, as it's a fine place to start when you don't yet know much biology, still less much biogerontology. I'm hoping that one day he will become curious enough about all this to get more informed and involved - but as is mentioned, he's quite busy doing a lot of other very valuable things already. Luckily, others of his ilk (notably Peter Thiel) are prioritising aging already.

##### To what extent, if any, does SENS Research Foundation watch for non-7-Causes longevity discoveries? (see details)
We absolutely watch for such things. Let me restate your question a little though. One thing we watch for is additional causes - eighth types of damage. We can reject them because of compelling evidence that they accumulate too slowly to matter in a currently normal lifetime; sometimes we need to do research to obtain such evidence, as with our project on epimutations at Einstein. The other reason for rejecting them is if there is compelling evidence that they will spontaneously reverse if we fix the existing seven. But your question is not with regard to new types of damage, but new types of fix. The question then is whether the fixes work by somehow overriding the seven damage types, or by fixing them, or by fixing an eighth damage type that we haven't yet characterised. To take the examples you cite:

The one about heterochromatin is a hot topic right now. It's closely related to our work at Einstein mentioned above. But this particular study tells us very little, because it's in a model of accelerated aging - it's easy to make cells or organisms unhappy at a younger age than usual, and that doesn't mean they get unhappy for that reason in normal conditions. As things stand, Im still betting that these changes happen too slowly to matter in a currently normal lifetime.

The one about blood infusions is of the other type. For sure the blood change sin composition in many ways during life, and those changes act to spread aging around the body - basically, to accelerate the aging of tissues that are doing relatively well, by exposing them to the problems of tissues that are doing relatively badly. But clearly if we can properly rejuvenate the latter class, the blood will come right on its own. Conversely, if we do this kind of infusion, yes it will have some benefit, but as the problematic tissues get older and older it will be less and less effective.

##### How promising is the ultrasound Alzheimer's treatment shown in Leinenga and Götz's March 2015 article?
It's definitely intriguing, and I agree with Jae, we need to know about the long term. If microglia can do this, why do they not do it already? The good news is that we are already pretty much there in terms of removing plaques using vaccination, so the focus has really turned to removing tangles and replacing lost neurons and reversing synaptic atrophy.

##### Why do we age? How does the aging process work? What can be done to stop the aging process?
See http://sens.org/ and my book Ending Aging.

##### What would it take to reverse presbyopia?
Basically just a crosslink-breaker that would restore the lens's elasticity. The molecular structure of lens crosslinks may not be the same as in collagen etc elsewhere in the body, so this may be some way off.

##### Does in-silico testing and development as mentioned in the video below seem like a prime candidate for the most fruitful avenue to pursue in the coming decades for disease and aging research and intervention?
"Candidate" is the wrong word - "component" is the right one. We will achieve proper control of aging by combining many technological advances: we need breakthroughs across the board. I'm quite sure that better ways to analyse large datasets will play a substantial part in that, and that's what this company are doing. I think they're doing it in a very promising way. Also, I think its contribution will become clear within a matter of years, not decades.

##### Do Cenegenics programs really work?
Before one can answer such a question, one needs to define the criterion. What do you really mean, quantitatively, by "it works"?

##### Based on the growing advancements in medicine and technology now and in the future, what is the predicted life expectancy of a 30-year-old?
Can't be predicted, because it depends on so many things - how safe cars become, how well we avoid asteroids, etc. First things first - aging is killing people today! Self-interest is a great motivator, but humanitarian considerations should come first.

##### Why can't we give our babies Foxo mutant genes that will give them longevity?
Germ line gene therapy hasn't been perfected yet, but the chances are that it will start to be used pretty soon for the elimination of certain congenital diseases, and once that starts I expect the floodgates will indeed open. But for longevity, no single genetic change will have much effect. Mutations  in FoxO and related genes have much weaker longevity effects in longer-lived species than in shorter-lived ones, basically because the evolutionary pressure to adapt to famines of a given length varies with the frequency of those famines and long famines are rarer than short ones. (See my 2005 paper in Gerontology for details.) I estimate that the most we could get from any such manipulation is a couple of years.

##### What would happen if the 10 richest people in the world each put half of their money towards negligible senescence research?
One thing that never ceases to bewilder me is the frequency with which people raise the same old fears about problems that would be created by solving today's biggest problem, and do so without betraying the faintest suspicion that anyone might have thought about such issues before. It's  breathtaking.

But returning to the original question: actually I think Tony has said pretty much everything I would want to say, in his detailed and excellent response. Many thanks Tony. It's not clear that $200 billion would be appreciably more effective than #2 billion in accelerating the research currently being done - I think $2 billion would suffice to cover pretty much all the bases and leave the sheer difficulty of the science as the rate-limiter - but for sure the subsequent phase, when this work moves from the lab to the clinic, will need very large investment (building new infrastructure, training more medics, etc), and the sooner that investment is forthcoming the more effective it will be in accelerating that phase and bringing agelessness to the masses.

##### Why is it important to understand and study the ageing process?
I agree with the other answers, and I would add this: not only all medicine but all technology consists of going against our evolved state, and I suspect you are generally in favour of the wheel, cell phones, etc, as well as vaccines etc. Aren't you shocked, now we've said these things, at your own bizarre idiocy in having asked the question (even to yourself)? I'll tell you what is shocking to me - that so many people think like your question.

##### I am working on a second book regarding comparative gerontology. Which books do you recommend for my research?
I agree with Marios (for once :-)). Finch's book is 25 years old this year, but does not obviously have a worthy successor.

##### If I am 30 now, what is the possibility that I could live to be 120, with the assumption that medical technology will progress enough in the next 50 years to allow this?  What technology is expected to prolong life in the future?
Well, that's kinda a tautological question - I mean, as of now the main uncertainty is precisely how fast the technology will progress. I could interpret your question as "what is my chance of living to the year 2065 without any such progress, in good enough health to be able to benefit from therapies that arrive at that time?" - to which the answer is probably about 50%, depending obviously on your family history, lifestyle etc. Or I could interpret it as "what is my chance of living until 2105 assuming I benefit from these therapies in 2065 at the age of 80?", to which my answer is probably in excess of 99%, given the progress that will also almost certainly have been made by then in reducing other risks of death.

##### In 2014, what would have been the expected lifespan of someone who did everything in their power, on an individual level, to not die?
The question is kinda backwards, isn't it? If someone is alive at the start of 2014 and does everything they can (within reason) not to die any time soon, they will maximise their chance of making it into 2015. Also, clearly since scientific knowledge is increasing, no one who dies at an advanced age in 2014 could have acted perfectly all their lives with respect to 2014 scientific knowledge. Why do you even care about the question in the form you posed it?

###### Comments
- Mati Roy: Another (and probably clearer) way to ask it would be: for someone who is 18 years old today and has always done and will always do everything in their power to survive, how long could s/he expect to live given our current technologies and knowledge (supposing it stays the same in the future; even if I know it won't). The reason is that I want to remove the speculations about the future from the answers. I will add the speculations myself (with the help of other sources; including your answers to other questions on Quora). I'd like to know how long I could expect to live if I was VERY careful given that current knowledge and technologies stayed the same. This would help me to plan for my future, for my life. This would also help me determine for whom this kind of effort is worth it. For example, if doing everything in one's power only increases one's life expectancy of X years, than I might not recommend it to Y type of people.
  
  So I'm still interested in knowing your answer to the original question. I don't think it's "kinda backwards".
  
  Thank you.
- Aubrey: OK, that's a much less "backwards" question since it fixes the date of birth (to 1997) rather than the date of death. I'd estimate 90-95.

  Also, your motivation for the question (this new one!) is good but not perfect. People absolutely need to know that their own actions, in the near term, will  impact the probability distribution of their and others' experience of aging in the distant future. But in practice, if you think about the maths, it's easy to see that the impact a single person (even someone as influential in the field as me) can have on the distant future of a single person (themselves or any other single person) is small to infinitesimal, because the range of uncertainty of when they will die in the absence of progress and the range of uncertainty of how rapidly the science will progress both greatly exceed the difference to those numbers that one person can realistically make. Therefore, the thing to get people to focus on is not their own prospects but the humanitarian argument, for which the maths is very different. If one decides tha everyone matters, not just oneself or one's loved ones, then one just needs to remember that every single DAY that one brings forward the defeat of aging is over 100,000 lives saved (not to mention all the associated alleviation of suffering). THAT is what gets me out of bed in the morning.
- Mati Roy: Why does fixing the date of birth matters if we consider 2014 knowledge and technologies? Oh, maybe I should have added with 2014 air pollution, and things like that. Thanks for your estimate!
- Aubrey: You guessed it. The main factor is changes in prosperity, leading to changes in early-life nutrition.

##### What is Google Calico doing this long?
They have a near-term strategy and a long-term one. All the press has been centred on the near-term one - the Abbvie deal etc. It's no surprise that they are not talking much about the long-term one, since it's, you know, long-term. However, they now have an actual in-house lab and they hired quite a few people in the past couple of months. I think they'll make a big contribution eventually.

##### Biotechnology: How hard would it be to artificially grow a body that can be used for a human head transplant?
Extremely hard, but most of all, extremely hard to control. If you want a new body, you want it to have the characteristics you choose, and that'd require a way to guide the growth. All in all my money is on printing it rather than growing it. But that's extremely hard too, don't get me wrong!

##### Would we effectively cure aging in most persons if we could: 1) prevent cancer 2) cure heart disease 3) cure neurodegenerative disease and 4) continue vigorous exercise regimens into old age?
You're asking the question the wrong way around. The correct question is "could we effectively cure 1) cancer 2) heart disease 3) neurodegenerative diseases without curing aging?" And the answer to that question is no. It is incorrect to think of any of the diseases of old age as separate, or even separable, from each other: they are all facets of the same network of accumulating damage.
